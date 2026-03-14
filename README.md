<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/easy-homelab-server-switch/docs-project-overview">
    <img src="https://github.com/easy-homelab-server-switch.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Easy Homelab Server Switch</h3>
<h4 align="center">» Server component «</h4>
  <p align="center">
    <a href="https://github.com/easy-homelab-server-switch/docs-project-overview/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#useful-shortcuts">Useful shortcuts</a>
      <ul>
        <li><a href="#project-overview-useful-shortcuts">Project overview</a></li>
        <li><a href="#cloudflare-useful-shortcuts">Cloudflare</a></li>
        <li><a href="#server-useful-shortcuts">Server</a></li>
        <li><a href="#microcontroller-useful-shortcuts">Microcontroller (ESP32)</a></li>
        <li><a href="#client-useful-shortcuts">Client</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting started</a>
    </li>
    <li>
      <a href="#components">Components</a>
      <ul>
        <li><a href="#main">Main</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#configuration-module">Configuration module</a></li>
        <li><a href="#mqtt-module">MQTT module</a></li>
        <li><a href="#network-module">Network module</a></li>
        <li><a href="#tls-module">TLS module</a></li>
        <li><a href="#environment">Environment</a></li>
        <li><a href="#paths">Paths</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- USEFUL SHORTCUTES -->
## Useful shortcuts
|Module|Repository|README|License|
| :- | :- | :- | :- |
|<a id="project-overview-useful-shortcuts"></a>Project overview|[![project-overview][project-overview-shield]][project-overview-url]|[![project-overview][readme-shield]][project-overview-readme-url]|[![project-overview][license-shield]][project-overview-license-url]|
|<a id="cloudflare-useful-shortcuts"></a>Cloudflare|[![cloudflare][cloudflare-shield]][cloudflare-url]|[![cloudflare][readme-shield]][cloudflare-readme-url]|[![cloudflare][license-shield]][cloudflare-license-url]|
|<a id="server-useful-shortcuts"></a>Server|[![server][server-shield]][server-url]|[![server][readme-shield]][server-readme-url]|[![server][license-shield]][server-license-url]|
|<a id="microcontroller-useful-shortcuts"></a>Microcontroller (ESP32)|[![microcontroller-esp32][microcontroller-shield]][microcontroller-url]|[![microcontroller-esp32][readme-shield]][microcontroller-readme-url]|[![microcontroller-esp32][license-shield]][microcontroller-license-url]|
|<a id="client-useful-shortcuts"></a>Client|[![client][client-shield]][client-url]|[![client][readme-shield]][client-readme-url]|[![client][license-shield]][client-license-url]|

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
# Getting started
This repository is part of the **Easy Homelab Server Switch** project.
If you are exploring it for the first time, start with the **[Project Overview README][project-overview-readme-url]** repository which explains the architecture and interaction between all components.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- COMPONENTS -->
# Components
The server MQTT agent is organized into small modules, each responsible for a specific part of the system.

<a id="main"></a>
### Main (main.py)
  - Orchestrates the application. 
  - Executes the system shutdown sequence using dbus-send to communicate with the host's power management service. 

<a id="configuration"></a>
### Configuration (config.py)
  - Defines the central dictionary for broker settings, credentials, and MQTT topic. 

<a id="configuration-module"></a>
### Configuration module (config_module.py)
  - Provides validation to ensure all critical parameters are present before the system attempts to start. 

<a id="mqtt-module"></a>
### MQTT module (mqtt_module.py)
  - Manages the secure TLS connection to the MQTT broker. 
  - Implements the Last Will and Testament (LWT) feature to automatically broadcast a `"DEAD"` state on `TOPIC_HEARTBEAT` if the agent loses connection (expectedly or unexpectedly). 
  - Subscribes to `TOPIC_SYSTEM` and triggers local actions based on incoming remote commands. 

<a id="network-module"></a>
### Network module (net_module.py)
  - Performs network validation by checking physical interface link states and system routing tables. 
  - Verifies actual internet reachability via low-level socket checks to public DNS server. 

<a id="tls-module"></a>
### TLS module (tls_module.py)
  - Manages the CA certificate required for secure MQTT communication. 
  - Ensures secure storage and retrieval of certificate data within the application's data directory. 

<a id="environment"></a>
### Environment (constants.py)
  - Defines shared constants used across the application.

<a id="paths"></a>
### Paths (paths.py)
  - Resolves and creates the application data directory.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

[microcontroller-shield]: https://img.shields.io/badge/Microcontroller-8A2BE2
[cloudflare-shield]: https://img.shields.io/badge/Cloudflare-8A2BE2
[client-shield]: https://img.shields.io/badge/Client-8A2BE2
[server-shield]: https://img.shields.io/badge/Server-8A2BE2
[project-overview-shield]: https://img.shields.io/badge/Project%20overview-8A2BE2
[readme-shield]: https://img.shields.io/badge/README-8A2BE2
[license-shield]: https://img.shields.io/badge/LICENSE-8A2BE2

[microcontroller-url]: https://github.com/easy-homelab-server-switch/esp32
[cloudflare-url]: https://github.com/easy-homelab-server-switch/cloudflare
[client-url]: https://github.com/easy-homelab-server-switch/client
[server-url]: https://github.com/easy-homelab-server-switch/server
[project-overview-url]: https://github.com/easy-homelab-server-switch/docs-project-overview

[microcontroller-readme-url]: https://github.com/easy-homelab-server-switch/esp32/blob/main/README.md
[cloudflare-readme-url]: https://github.com/easy-homelab-server-switch/cloudflare/blob/main/README.md
[client-readme-url]: https://github.com/easy-homelab-server-switch/client/blob/main/README.md
[server-readme-url]: https://github.com/easy-homelab-server-switch/server/blob/main/README.md
[project-overview-readme-url]: https://github.com/easy-homelab-server-switch/docs-project-overview/blob/main/README.md

[microcontroller-license-url]: https://github.com/easy-homelab-server-switch/esp32/blob/main/LICENSE
[cloudflare-license-url]: https://github.com/easy-homelab-server-switch/cloudflare/blob/main/LICENSE
[client-license-url]: https://github.com/easy-homelab-server-switch/client/blob/main/LICENSE
[server-license-url]: https://github.com/easy-homelab-server-switch/server/blob/main/LICENSE
[project-overview-license-url]: https://github.com/easy-homelab-server-switch/docs-project-overview/blob/main/LICENSE