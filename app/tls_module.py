import os

from constants import CERT_FILENAME
from config import MQTT_CA_CERTIFICATE_CONTENT
from paths import get_app_data_dir

def ensure_cert_file() -> str | None:
    cert_dir = get_app_data_dir()
    certh_path = os.path.join(cert_dir, CERT_FILENAME)

    if not os.path.exists(certh_path):
        if not MQTT_CA_CERTIFICATE_CONTENT:
            return None

        with open(certh_path, "w", encoding="utf-8") as file:
            file.write(MQTT_CA_CERTIFICATE_CONTENT)

    return certh_path