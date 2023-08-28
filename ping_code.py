import board
import busio
import time
import digitalio
from adafruit_esp32spi import adafruit_esp32spi

# Get WiFi details from your settings.py file
from settings import settings

# Define the pins used by the BitsyExpander's ESP32 WiFi module
esp32_cs = digitalio.DigitalInOut(board.D9)
esp32_ready = digitalio.DigitalInOut(board.D11)
esp32_reset = digitalio.DigitalInOut(board.D12)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Initialize the ESP32 WiFi module
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("\nESP32 WiFi Module found.")
    print("Firmware version:", str(esp.firmware_version, "utf-8"))
    print("*" * 40)

print("\nScanning for available networks...\n")
network_list = [str(ap["ssid"], "utf-8") for ap in esp.scan_networks()]
if settings["ssid"] not in network_list:
    print(settings["ssid"], "not found.\nAvailable networks:", network_list)
    raise SystemExit(0)

print(settings["ssid"], "found. Connecting...")
while not esp.is_connected:
    try:
        esp.connect_AP(settings["ssid"], settings["password"])
    except (RuntimeError, ConnectionError) as e:
        print("\nUnable to establish connection. Are you using a valid password?")
        print("Error message:", e, "\nRetrying...")
        continue

print("Connected! IP address:", esp.pretty_ip(esp.ip_address))

while True:
    print("\nPinging google.com...")
    response = esp.ping("google.com")
    print("Ping successful. Response time:", response, "ms")
    time.sleep(5)
