<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/easy-homelab-server-switch/docs-project-overview">
    <img src="https://github.com/easy-homelab-server-switch.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Easy Homelab Server Switch</h3>
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
[about-the=project-url]: https://ehss.github.mikolajadamczyk.tech/

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


Key Components
1. MQTT Module (mqtt_module.py)

    Secure Connection: Implements TLS encryption

    Last Will and Testament (LWT): Automatically notifies the system if the agent goes "DEAD" unexpectedly.

    Command Handling: Subscribes to the system topic to execute remote power commands.

2. Network Monitoring (net_module.py)

    Multi-layered Check: Validates the physical link state, routing tables, and DNS reachability (socket check to 8.8.8.8).

    Automatic Recovery: Designed to handle reconnections gracefully without crashing during network outages.

3. Power Management (main.py)

    System Integration: Uses dbus-send to communicate with the host's systemd-logind service.

    Graceful Shutdown: Sends a final "DEAD" state to the broker via Last Will after the physical power-off sequence.