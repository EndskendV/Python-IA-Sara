import hashlib
import psutil

def generate_user_id():
    # Obtener el identificador del disco duro (serial number)
    try:
        disk_info = psutil.disk_partitions()
        for partition in disk_info:
            if partition.device.startswith('/'):
                serial_number = psutil.disk_usage(partition.device).serial
                break
    except Exception:
        serial_number = ""

    # Obtener la dirección MAC de la tarjeta de red
    try:
        import uuid
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except Exception:
        mac_address = ""

    # Combinar los componentes y generar el identificador único
    user_id_data = f"{serial_number}{mac_address}"
    user_id = hashlib.sha256(user_id_data.encode()).hexdigest()

    return user_id

if __name__ == "__main__":
    user_id = generate_user_id()
    print(f"User ID: {user_id}")
