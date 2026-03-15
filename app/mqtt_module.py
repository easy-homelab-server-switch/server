import ssl
import uuid
import paho.mqtt.client as mqtt

from config import MQTT_CONFIG, TOPICS
from tls_module import ensure_cert_file
from net_module import check_internet_connection

class MqttModule:
    def __init__(self, on_system_command=None):
        self.client = None
        self.on_system_command = on_system_command
        self.is_shutting_down = False

    def start(self):
        client_id = f"ServerAgent-{uuid.uuid4().hex[:6]}"
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)
        self.client.username_pw_set(MQTT_CONFIG["user"], MQTT_CONFIG["pass"])

        self.tls_setup()

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        self.client.will_set(TOPICS["heartbeat"], payload="DEAD", qos=1, retain=True)

        print(f"MQTT: Connecting with ID: {client_id} to {MQTT_CONFIG['ip']}...")
        self.client.connect_async(MQTT_CONFIG["ip"], MQTT_CONFIG["port"], 60)

        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.loop_forever()

    def stop(self):
        if not self.is_connected():
            return
        self.client.loop_stop()
        self.client.disconnect()
        
    def tls_setup(self):
        cert_path = ensure_cert_file()

        if not cert_path:
            print("TLS: Without certificate")
            self.client.tls_set(cert_reqs=ssl.CERT_NONE)
            self.client.tls_insecure_set(True)
            return

        print("TLS: With certificate")
        self.client.tls_set(ca_certs=cert_path, tls_version=ssl.PROTOCOL_TLSv1_2)

    def is_connected(self) -> bool:
        print("MQTT: Checking connection...")
        is_ok = (self.client and self.client.is_connected())

        if not is_ok:
            print("MQTT: No client.")

        return is_ok

    def subscribe(self, topic: str):
        if not self.is_connected():
            return

        result, _ = self.client.subscribe(topic)
        if result == mqtt.MQTT_ERR_SUCCESS:
            print(f"MQTT: Subscribed to topic {topic}.")
        else:
            print(f"MQTT: Failed to subscribe to topic {topic}.")

    def publish_heartbeat(self, state: str):
        if not self.is_connected():
            return

        print("MQTT: Publishing heartbeat")
        result = self.client.publish(TOPICS["heartbeat"], state, retain=True)
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print("MQTT: Published message.")
        else:
            print("MQTT: Failed to publish message.")
            
    def reconnect(self):
        print("MQTT: Reconnect attempt...")
        try:
            self.client.reconnect()
        except Exception as e:
            print(f"MQTT: Reconnect error: {e}")

    def on_connect(self, client, userdata, flags, rc, props=None):
        if rc == 0:
            print("MQTT: Connected!")
            self.subscribe(TOPICS["system"])
            self.publish_heartbeat("ALIVE")
        else:
            print(f"MQTT: Connection error! rc={rc}.")

    def on_disconnect(self, client, userdata, flags, rc, props=None):
        if self.is_shutting_down:
            return

        print("MQTT: Disconnected!")
        if not check_internet_connection():
            return

        code = rc.value if hasattr(rc, "value") else rc
        print(f"MQTT: Disconnect code: {code}")

    def on_message(self, client, userdata, msg):
        if self.is_shutting_down:
            return

        payload = msg.payload.decode().strip().upper()
        print(f"MQTT: Received on topic: {msg.topic}. Message: {payload}")

        if msg.topic == TOPICS["system"] and self.on_system_command:
            self.on_system_command(payload)