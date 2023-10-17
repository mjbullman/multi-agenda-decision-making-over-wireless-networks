#!/usr/bin/env python  
"""
            Insight Center for Data Analytics

                 University College Cork

                  Intel Galileo Client 3

    @author - Martin Bullman
    @since - 03/07/2014
"""

import socket   
import collections
from pyGalileo import *

HOST = ''   				 # Symbolic name meaning all available interfaces
PORT = 9999      			 # Port number that all devices will use to communicate
SHORT_DELAY = .1			 # Short delay before socket times out
LARGE_DELAY = .5			 # Large delay before socket times out
SAMPLE_RATE = 50			 # Sample rate at which sounds are detected
BUFFER_SIZE = 1024			 # Maximum size of receive buffer in bytes
LISTEN_WINDOW = 500			 # Time in millis to listen for sounds
LOCAL_HOST = '192.168.1.223'  
BCAST_ADDR = '192.168.1.255' # Subnet broadcast address

redLed = 3
amberLed = 2
soundLed = 4   
inNeighbours = {}         	 # Store nodes that have been discovered as in neighbours
soundDetected = False

# Configures three Intel Galileo GPIO pins to be used as outputs.
#
# As you can see from the variables above we are using pins 2, 3,
# and 4 on the Intel Galileo this enables us to switch the LEDs
# on and off easily. also note pin 3 is a pulse width modulation 
# pin and that we require the pyGalileo python library to easily
# interact with the GPIO pins on the Intel Galileo.
#------------------------------------------------------------------------------------------------------------------------
def setupLeds( ):
#------------------------------------------------------------------------------------------------------------------------
    pinMode( redLed, OUTPUT )
    pinMode( amberLed, OUTPUT )
    pinMode( soundLed, OUTPUT )

# Switches on the correct LEDs before we begin listening for sounds
#	
# Set the LEDs up by switches on and off all the LEDs so that only 
# the correct LED is illuminated at the start of the program. Just 
# the red LED should be illuminated at the beginning.
#------------------------------------------------------------------------------------------------------------------------
def flickerLights( ):
#------------------------------------------------------------------------------------------------------------------------
    digitalWrite( soundLed, HIGH )
    delay( 750 )
    digitalWrite( soundLed, LOW )
    digitalWrite( amberLed, HIGH )
    delay( 750 )
    digitalWrite( amberLed, LOW )
    digitalWrite( redLed, HIGH )

# Discovers all the nodes that are in range of this device.
#
# We broadcast a 'who's there' message to every node connected to
# our ad-hoc network. Every node that receives the message will
# reply. We then store the IP addresses of all the replying nodes 
# in a hash table in which we will also store there sound levels. 
#-------------------------------------------------------------------------------------------------------------------------	
def nodeDiscovery( ):
#-------------------------------------------------------------------------------------------------------------------------
    global inNeighbours

    print('Scanning...')
    # Broadcast packet to every IP address on the subnet
    peerSocket.sendto( 'Who\'s There!', ( BCAST_ADDR, PORT ) )

    # Listen for one second to receive incoming packets from relying nodes
    peerSocket.settimeout( SHORT_DELAY * 20 )
    while True:
        try:
            # Receive incoming replies from the socket
            digitalWrite( amberLed, HIGH )
            message, address = peerSocket.recvfrom( BUFFER_SIZE )
            print('I\'m Here: ', address[0])

            # If address is not in this nodes hash table, add it
            if address[0] not in inNeighbours:
                inNeighbours[ address[0] ] = 0
            digitalWrite( amberLed, LOW )
        # If socket times out stop listening for replies
        except socket.timeout:
            print('No more peer\'s found!\n')
            digitalWrite( amberLed, LOW )
            break

    # Sort the hash table by IP addresses
    inNeighbours = collections.OrderedDict( sorted( inNeighbours.items( ) ) )
    # Print list of known nodes who replied to the broadcast message
    print('List of in Neighbours: ', inNeighbours)


# Listen for analog sounds in the environment and return the levels	
#
# The Audio signal from the output of the sound sensor is a varying 
# voltage. To measure the sound level we need to take multiple 
# measurements to find the minimum and maximum extents or "peak to
# peak amplitude of the signal. We used a sample window of 50ms. 
# That is sufficient to measure sound levels of frequencies as low
# as 20Hz - The lower limit of human hearing.
#------------------------------------------------------------------------------------------------------------------------
def getSoundLevel( ):
#------------------------------------------------------------------------------------------------------------------------
    startMillis = millis( )                                 	# Start of sample window
    signalMin = BUFFER_SIZE										# Set signal min to max buffer size
    signalMax = 0

    # Collect sound sensor data for 50ms
    while millis() - startMillis < SAMPLE_RATE:
        # Read data from Analog sound sensor
        sample = analogRead( A0 )

        if sample < BUFFER_SIZE:                        		# toss out spurious readings
            if sample > signalMax:
                signalMax = sample                          	# save just the max levels
            elif sample < signalMin:
                signalMin = sample                          	# save just the min levels

    # Return the peak to peak value of the sound
    return signalMax - signalMin

# Prints the sound level to the screen 
#
# also switches on and off the green LEDto indicate that a 
# sound has been detected by the sound sensor.	
#------------------------------------------------------------------------------------------------------------------------
def printSoundLevel( ):
#------------------------------------------------------------------------------------------------------------------------
    digitalWrite( soundLed, HIGH )
    print('Sound Level: ', peakToPeak)
    digitalWrite( soundLed, LOW )


# Delay function that will delay our client by a given time.
#
# Used before each node transmits a zero to prevent collisions
# where many nodes transmit a zero at the same time.	
#------------------------------------------------------------------------------------------------------------------------
def waitRandomTime( time ):
#------------------------------------------------------------------------------------------------------------------------	
    while time >= 0.00:
        print('Waiting...')
        time -= 0.01

# Starts a sequence in which all nodes will transmit their sound
# levels. Each node will transmit in ID sequence until all nodes
# had transmitted their sound levels. Each node will store the sound
# levels of the other nodes which will enable it to decide which 
# node had the highest sound level and therefore was the winner.
#------------------------------------------------------------------------------------------------------------------------
def startSendingSequence( ):
#------------------------------------------------------------------------------------------------------------------------	
    numLoops = len( inNeighbours ) + 1                           # The number of iterations we have to make
    currentHostNum = 1
    lastHost = 0
    heardNodes = []

    # While there is more nodes to transmit there sound level
    while currentHostNum <= numLoops:
        digitalWrite( amberLed, HIGH )
        # Get the next node in the list
        currentHostAddr = '192.168.1.22' + str( currentHostNum )

        # If this node is the next in the sequence then broadcast its sound level to all nodes
        if LOCAL_HOST == currentHostAddr:
            peerSocket.sendto( str( peakToPeak ), ( BCAST_ADDR, PORT ) )

        # Accept the sound level being broadcast.
        try:
            peerSocket.settimeout( LARGE_DELAY )
            message, address = peerSocket.recvfrom( BUFFER_SIZE )
            print('Message Received!')
            print('Peer:', address[0], ' Said: ', message)

            # If packet arrives out of sequence and this node did not already hear from the node resend the sound level
            if len( message ) <= 5 and int( address[0][12:] ) - lastHost > 1:
                if '192.168.1.22' + str( int( address[0][12:] ) - 1 ) not in heardNodes:
                    print("out of sequence")
                    peerSocket.sendto( 'SR 192.168.1.22' + str( int( address[0][12:] ) - 1 ), ( '192.168.1.22' + str( int( address[0][12:] ) - 1 ), PORT ) )
                    numLoops += 1
            # If this node receives an out of sequence message resend the sound level
            if message[:1] == 'S':
                print('resent out of sequence packet')
                peerSocket.sendto( str( peakToPeak ), ( address[0], PORT ) )
                numLoops += 1

            # if the message contains an R and is addressed to this node, resend sound level
            if message[:1] == 'R' and message[2:] == LOCAL_HOST:
                peerSocket.sendto( str( peakToPeak ), ( address[0], PORT ) )
                numLoops += 1

            # If message contains an R and is not addressed to this node backoff so the resent
            # message can propagate the network
            if message[:1] == 'R' and message[2:] != LOCAL_HOST:
                numLoops += 1

            # If the address of the node is not all ready in the list, add it
            if address[0] in inNeighbours and message[:1] != 'R' and message[:1] != 'S':
                inNeighbours[ address[0] ] = int( message )

            if len( message ) <= 5:
                lastHost = int( address[0][12:] )
                if address[0] not in heardNodes:
                    heardNodes += [address[0]]
            #print address[0][12:]
            #print heardNodes
        # If the socket times out and we dont receive a level from the node we expect
        # ask that node to resent its sound level by sending it an R message
        except socket.timeout:
            print('No reply! Socket timed out!')

            if int( currentHostAddr[12:] ) <= len( inNeighbours ):
                print('Asking node to resend data')
                peerSocket.sendto( 'R ' + currentHostAddr, ( BCAST_ADDR, PORT ) )

        currentHostNum += 1				   # Move onto next node in the sequence
        digitalWrite( amberLed, LOW )

# The main function, program starts here	
#------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
#------------------------------------------------------------------------------------------------------------------------
    # Configure three Galileo's pins for use as outputs
    setupLeds( )
    # Sets the Led lights for the beginning of the program
    flickerLights( )

    # Create a socket, used in accepting connections from peers
    try:
        print('*** I am Client 3 ***\n')
        peerSocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP )
        peerSocket.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1 )
    except socket.error as errorMsg:
        print('Failed to create socket. Error Code : ' + errorMsg[0] + ' Message ' + errorMsg[1])

    # Bind the socket to its local address and port number.
    try:
        peerSocket.bind( ( HOST, PORT ) )
        print('UDP socket bind complete!')
    except socket.error as errorMsg:
        print('Bind failed. Error Code : ', errorMsg[0], ' Message ', errorMsg[1])

    # Discover nodes in range.
    nodeDiscovery( )

    # Never ending loop, that alternates between two inner loops
    while True:
        # Store the current millis second timestamp
        startMillis = millis( )

        # Listen for sound samples for a given time
        print('\nClient Listening For Sound')

        while millis() - startMillis < LISTEN_WINDOW:
            # Get the sound level
            peakToPeak = getSoundLevel( )

            # If sound level is less than the threshold
            if peakToPeak < 0:
                print('No Sound!')
            else: # print the level, begin the communication sequence
                soundDetected = True
                # Print the sound level, switch on sound LED
                printSoundLevel( )
                delay( 200 )
                break

        # Accept incoming connections from other nodes till no more remain.
        while True:
            if soundDetected:
                # Wait for a random time before broadcasting a zero, to avoid collisions with other
                # nodes broadcasting a zero.
                # randTime = random.uniform( 0.00, 0.05)
                # waitRandomTime( randTime )
                # Broadcast a zero from this node to all nodes on the network, to indicate a sound
                # has been detected.
                peerSocket.sendto( '0', ( BCAST_ADDR, PORT ) )
                soundDetected = False

            print('\nSocket Listening For Connections!')

            try:
                # Listen for connections until socket times out
                peerSocket.settimeout( SHORT_DELAY )
                message, address = peerSocket.recvfrom( BUFFER_SIZE )
                print('Peer:', address[0], ' Said: ', message)

                # Set the LEDs after accepting connection
                digitalWrite( redLed, LOW )

                if message[:1] != 'W':
                    digitalWrite( amberLed, HIGH )
            except socket.timeout:
                print('Socket Timed Out!')
                break

            # If we receive a Who's There message, we add that nodes address to the list of nodes
            if message == 'Who\'s There!':
                if address[0] not in inNeighbours:
                    inNeighbours[ address[0] ] = 0
                    inNeighbours = collections.OrderedDict( sorted( inNeighbours.items( ) ) )
                digitalWrite( amberLed, LOW )
                # Send a reply to the node so they can also add this nodes address to there list of nodes
                peerSocket.sendto( '', ( address[0], PORT ) )

            # If we receive a zero message it means another node has detected a sound
            if message == '0':
                # If more than one node detects a sound, they will all broadcast zeros
                # So we must handle them first before we begin the coordinated sequence
                while True:
                    try:
                        peerSocket.settimeout( .2 )
                        data = peerSocket.recvfrom( BUFFER_SIZE )
                        print(data[1][0], ' also detected sound!')
                    except socket.timeout:
                        print('Socket Timed Out!\n')
                        break

                # Delay one second to make sure all zeros have been handled
                delay( 1000 )

                # Start the coordinated sequence protocol
                startSendingSequence( )
                # Find the winner by getting the address with highest sound level
                Winner = max( inNeighbours, key=inNeighbours.get )
                print('\nWinner: ', Winner)

                # The winning node will turn on the green LED and broadcast a 'W' message
                if Winner == LOCAL_HOST:
                    digitalWrite( soundLed, HIGH )
                    delay( 3000 )
                    peerSocket.sendto( 'W', ( BCAST_ADDR, PORT ) )
                    digitalWrite( soundLed, LOW )
                # While all the other nodes will switch on the red LED
                else:
                    digitalWrite( redLed, HIGH )
                    delay( 3000 )

                # Receive the 'W' message
                try:
                    message, address = peerSocket.recvfrom( BUFFER_SIZE )
                    print('Peer:', address[0], ' Said: ', message)
                except socket.timeout:
                    print('Socket Timed Out!\n')
                    break

            # Reset the lights before we start listening for sounds again
            digitalWrite( soundLed, LOW )
            digitalWrite( redLed, HIGH )
        peerSocket.close()  # Close the socket connection
    # end main loop