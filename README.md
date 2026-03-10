Easy Homelab Server Switch - Server
System Role

The MQTT Agent is a Python-based service running as a Docker container on the physical server. Its primary responsibility is to listen for system commands (like SHUTDOWN) via a secure MQTT channel and monitor the server's network health.

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