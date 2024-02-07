<p align="center">
    <img src="https://www.insight-centre.org/wp-content/uploads/2020/03/INSIGHT-LOGO-WHITE-1.png" width="500" alt="Insights Logo" />
</p>

<h1 align="center">
    Multi Agenda Decision-Making Over Wireless Networks
</h1>

<p align="center">
    <em>
        The demand for real-time decision-making, propelled by diverse data sources, is increasingly significant
        across various industry sectors. Conventional applications typically entail collecting data from an array
        of widely distributed sensors, transmitting it to a centralized access point for informed decision-making.
        The resultant decisions are then communicated to remote actuators, enabling devices to perform tasks based
        on the outcomes.
    </em>
</p>

<p align="center">
    <em>
        In response to this imperative, we researched and constructed a testbed for real-time decision-making over
        wireless networks. This involved utilizing multiple Intel Galileo embedded microcontrollers and implementing
        a novel protocol that exemplified the principles of sensing, communication, actuation, and coordination.
   </em>
</p>

<p align="center">
    <em>
       The project and its noteworthy findings were documented and published in the 2014 Insight Research Center for
        Data Analytics Annual Conference. Supported by Science Foundation Ireland (SFI) Grant SFI/12/RC/2289.
    </em>
</p>

<p align="center"> 
    <a href="https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/blob/main/docs/multi_agent_decision_making_over_wireless_networks_paper.pdf">Research Paper</a> |
    <a href="https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/blob/main/docs/multi_agent_decision_making_over_wireless_networks_poster.pdf">Research Poster</a> |
    <a href="https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/blob/main/docs/multi_agent_decision_making_over_wireless_networks_project_report.pdf">Project Report</a>
</p>

<p align="center">
    <img src="https://img.shields.io/github/license/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks" alt="GitHub License" >
    <img src="https://img.shields.io/github/last-commit/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks" alt="GitHub last commit">
    <img src="https://img.shields.io/github/languages/top/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks" alt="GitHub top language">
    <img src="https://img.shields.io/github/issues/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks" alt="GitHub issues">
<p>

<hr>

##  Quick Links

> - [Overview](#overview)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Repository Structure](#repository-structure)
> - [Getting Started](#getting-started)
>   - [Prerequisites](#prerequisites)
>   - [Installation](#installation)
>   - [Setting Up the Wireless Test Bed](#setting-up-the-wireless-test-bed)
>   - [Running the Demonstration Application](#running-the-demonstration-application)
> - [Contributing](#contributing)
> - [License](#license)
> - [Acknowledgments](#acknowledgments)

##  Overview

Real-time decision-making with diverse data is increasingly vital across industries, typically involving data 
collection from various sensors, centralized processing, and subsequent actions by remote actuators. However, 
the conventional centralized communication process proves sluggish for real-time decisions. To address this, 
the project aimed to establish a decentralized communication system, allowing devices to transmit data directly
to every connected device for decision-making, eliminating the need for a central access point.

The project involved building a wireless testbed using Intel Galileo microcontrollers, extending them with 
breadboard, sensors, and LEDs. The developed demonstration application showcased the platform's capabilities in
decentralized data processing. Initial research included studying ad-hoc wireless networks through literature, 
online articles, and presentations, providing valuable insights into project concepts.

---

##  Features

1. <b>Decentralized Communication:</b> The project focuses on eliminating the bottleneck of centralized communication
in real-time decision-making by implementing a decentralized communication model. Devices transmit data directly to
every connected device, allowing for quicker decision-making without relying on a central access point.


2. <b>Intel Galileo Wireless Test Bed:</b> Successful construction of a wireless test bed using multiple Intel Galileo
microcontrollers. Integration of Intel Centrino N-135 Wi-Fi cards to enable wireless communication among the Galileo
boards. Extended the microcontrollers with bread boards, sensors and LED's.


3. <b>Ad-Hoc Wireless Network:</b> Manual configuration of ad-hoc wireless networks on Galileo devices, enabling
direct communication among connected devices. Script automation for ad-hoc setup, streamlining the process for 
efficiency and ease of use.


4. <b>Demonstration Application:</b> Construction of a demonstration application showcasing the capabilities of 
the wireless test bed. Extension of Galileo microcontrollers with sensors and LEDs, enabling data gathering, 
wireless transmission, decision-making, and visual representation of results.


5. <b>Coordinated Sequenced Protocol:</b> Development of a coordinated sequence protocol for multi-agent 
decision-making. Implementation of a sound-based protocol where devices communicate, share sound levels, and 
collectively determine the closest sound source.

---

## Technologies Used

### Python Programming Language

Python programming language is used for developing the coordinated sequence protocol client. Python scripts are 
executed on the Galileo boards to facilitate communication, decision-making, and LED control.

### Intel Galileo Development Boards:

The project is built around five Intel Galileo Gen 2 development boards, which are Arduino-certified and run a Yocto
Linux image as the operating system.

### Bash Scripting:

Bash scripts are used for automating the setup of ad-hoc wireless networks on the Galileo devices, streamlining the
configuration process.

### Arduino IDE:

The Arduino IDE is utilized for upgrading the firmware on the Intel Galileo boards. It enables users to write programs
(sketches) for the Galileo and upload them using the serial port.

### Networking Protocols:

Ad-hoc networking is configured manually using Linux commands to set up wireless communication among the Galileo 
devices. The coordinated sequence protocol is designed for multi-agent decision-making.

### Yocto Linux:

The Yocto Linux operating system is used as the primary OS on the Intel Galileo boards. It provides the basic 
functionality of a standard Linux OS and is tailored for embedded systems.

--- 

##  Repository Structure

```sh
└── multi_agent_decision_making_over_wireless_networks
    ├── docs
        ├── multi_agent_decision_making_over_wireless_networks_paper.pdf
        ├── multi_agent_decision_making_over_wireless_networks_poster.pdf
        ├── multi_agent_decision_making_over_wireless_networks_project_report.pdf
    ├── libs
        ├── pygalileo
            ├── examples
                ├── __init__.py
                ├── analog_input.py
                ├── array.py
                ├── blink.py
                ├── button.py
                ├── digital_read_serial.py
                ├── digital_read_speed.py
                ├── fade.py
                ├── fast.py
            ├── __init__.py
            ├── constants.py
            ├── galileo_pins.py
            ├── how_to_develop.txt
            ├── README.md
    ├── scripts
        ├── ad_hoc_1.sh
        ├── ad_hoc_2.sh
        ├── ad_hoc_3.sh
        ├── ad_hoc_4.sh
        ├── ad_hoc_5.sh
    ├── src
        ├── client_1.py
        ├── client_2.py
        ├── client_3.py
        ├── client_4.py
        ├── client_5.py
```

---

##  Getting Started

### Prerequisites
<em>Before you begin, ensure that you have the following:</em>

1. <b>Intel Galileo Development Boards (5x):</b> Donated by Intel for this project.


2. <b>Intel Centrino N-135 Wi-Fi Cards (5x) and Antennas (5x):</b> Provided along with the Galileo boards.


3. <b>Micro SD Cards (5x):</b> Required for booting the Galileo boards with the Yocto Linux image.


4. <b>Sound Sensors (5x), LEDs (5x Red & 5x Green), Breadboard (5x),  Resistors, Jumper Cables:</b>
Refer to the hardware components section in the documentation for a detailed list.

###  Installation

1. Clone the repository to your local machine:

```sh
git clone https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks.git
```

2. Navigate to the project directory:

```sh
cd multi-agenda-decision-making-over-wireless-networks
```

### Setting Up the Wireless Test Bed

1. <b>Installing Wi-Fi Cards:</b> Attach the provided expansion plate to the Intel Centrino Wi-Fi card, connect 
the Wi-Fi antenna, and install the Wi-Fi card onto the Galileo board.


2. <b>Upgrading Firmware:</b> Download and install the Arduino IDE. Connect the Galileo board to your computer,
launch the IDE, select the Galileo board, and upgrade the firmware following the provided steps. 


3. <b>Booting from SD Card:</b> Download the Linux image from the provided link, extract files to the micro SD card,
and boot the Galileo board with the new Linux OS.


4. <b>Remote Login via SSH:</b> Find the IP address of the Galileo board using an IP scanner. Use PuTTY to SSH into
the board with the default username 'root' and no password.


5. <b>Setting Up Ad-Hoc Wireless Network:</b> Manually configure ad-hoc networking using Linux commands. Repeat the
process for all Galileo devices. Bash scripts are provided for automation.


6. <b>Connecting Your Computer:</b> Locate the GalileoAD-HOC network on your computer and connect using the 
provided WEP security key.

### Running the Demonstration Application

1. <b>Assembling Hardware Components:</b> Connect power and ground cables, sound sensor analog output, install 
sound sensors, and set up LEDs. Refer to the hardware assembly section in the documentation for detailed 
instructions.


2. <b>Running the Coordinated Protocol Client:</b> Run the coordinated sequence protocol client by typing the
appropriate Python command in the terminal for each device.


3. <b>Node Discovery:</b> The coordinated protocol initiates with node discovery. Nodes broadcast "Who's There"
messages to dynamically locate and identify nearby nodes.


4. <b>Hash Table Usage:</b> Hash tables are utilized during the decision-making process to store and manage sound
levels from each device.


5. <b>Resending Mechanism:</b> A resending mechanism is implemented to ensure reliable data transmission in case of
packet loss or out-of-sequence reception.

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/discussions)**: Share your insights, provide feedback, or ask 
questions.
- **[Report Issues](https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/issues)**: Submit bugs found or log feature requests for 
Interoperability-of-cloud-monitoring-data.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your 
GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a
Git client.
   ```sh
   git clone https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive
name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project 
repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the 
[LICENSE](https://github.com/Martin-Bullman/multi-agenda-decision-making-over-wireless-networks/blob/main/LICENSE.md) 
file for details.

---

##  Acknowledgments

I would like to express my sincere gratitude to the following individuals and organizations for their 
invaluable contributions and support throughout the duration of this project:

### University College Cork (UCC):

A special thank you to UCC for providing a conducive environment for research and learning. The academic 
resources and facilities at UCC have been instrumental in the successful completion of this project.

### Insight Centre for Data Analytics:

I am deeply grateful to the Insight Centre for Data Analytics at UCC for hosting and supporting my summer 
internship. The collaborative and innovative atmosphere at Insight has significantly enriched my learning 
experience.

### Supervision by Ken Brown:

My sincere appreciation goes to Kenneth Brown for serving as my supervisor during this internship. His
guidance, expertise, and constructive feedback have been crucial in shaping the project and enhancing its
quality.

### Mentorship by Mohamed Wahbi:

I would like to extend my thanks to Mohamed Wahbi for being a dedicated mentor throughout this internship. 
His insights, encouragement, and technical assistance have played a vital role in the successful execution
of the "Multi-Agent Decision Making over Wireless Networks" project.

<br>
This project would not have been possible without the collective support and encouragement from these 
individuals and organizations. Their commitment to fostering a collaborative and intellectually stimulating
environment has left a lasting impact on my professional and academic journey.

Thank you for the opportunity and guidance.

[**Return To Quick Links**](#quick-links)
