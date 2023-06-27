import subprocess

def get_ip_address():
    try:
        # Ejecutar el comando para obtener la dirección IP
        output = subprocess.check_output(['ipconfig']).decode('latin-1')
        # Filtrar la salida para obtener la dirección IP
        lines = output.split('\n')
        ip_address = None
        for line in lines:
            if 'IPv4 Address' in line:
                ip_address = line.split(':')[1].strip()
                break
        return ip_address
    except subprocess.CalledProcessError:
        print("No se pudo obtener la dirección IP.")
        return None

def get_wifi_info():
    try:
        # Ejecutar el comando para obtener la información de la red WiFi
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('latin-1')
        # Filtrar la salida para obtener el SSID de la red WiFi
        lines = output.split('\n')
        ssid = None
        for line in lines:
            if 'SSID' in line:
                ssid = line.split(':')[1].strip()
                break
        return ssid
    except subprocess.CalledProcessError:
        print("No se pudo obtener la información de la red WiFi.")
        return None

# Obtener y mostrar la dirección IP
ip_address = get_ip_address()
if ip_address:
    print(f"Dirección IP: {ip_address}")

# Obtener y mostrar la información de la red WiFi
wifi_info = get_wifi_info()
if wifi_info:
    print(f"Red WiFi: {wifi_info}")
