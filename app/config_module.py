from config import MQTT_CONFIG, TOPICS

def validate_config() -> list[str]:
    errors: list[str] = []
    
    to_validate = [
         ("MQTT_CONFIG", MQTT_CONFIG),
         ("TOPICS", TOPICS),
    ]
    
    for label, cfg in to_validate:
        for key, value in cfg.items():
            if value in ("", None):
                errors.append(f"{label}.{key} is empty.") 
                
    return errors