import os
import sys
import time

from mqtt_module import MqttModule
from config_module import  validate_config

def handle_system_command(cmd: str, mqtt: MqttModule):
    try:
        if cmd == "SHUTDOWN":
            mqtt.is_shutting_down = True

            mqtt.stop()
            time.sleep(1)

            print("Shutting down the system...")
            cmd = "dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.PowerOff boolean:true"
            os.system(cmd)
            sys.exit()
    except Exception as e:
            print(f"EXCEPTION: in handle_system_command: {e}")
            
def is_config_ok() -> bool:
    errors = validate_config()
    if errors:
        for error in errors:
            print(f"Config error: {error}")
        return False
            
    return True
        
if __name__ == "__main__":
    if not is_config_ok():
        sys.exit(1)
    
    mqtt = MqttModule()
    mqtt.on_system_command = lambda cmd: handle_system_command(cmd, mqtt)
    try:
        mqtt.start()
    except Exception as e:
        print(f"EXCEPTION: in setup: {e}")