from components.wifi_setup import WiFi
from components.mqtt_setup import MQTTBroker
from SimpleOSC import SimpleOSCParser
from IEOSC import IEOSC
from timer import Timer
import random

# All messages in this list will be send as part of the
offline_messages = ["350", "370"]

offline_timer = Timer()
offline_timer.set_duration(5)

class EcoSystem:
    def __init__(self, ecosystem, creature, connect_to_ecosystem):
        self.connect_to_ecosystem = connect_to_ecosystem
        self.creature = creature
        if self.connect_to_ecosystem:
            self.wifi = WiFi()
            self.parser = SimpleOSCParser()
            self.OSCCommunicator = IEOSC(self.wifi.esp, self.wifi.socket, self.parser)

    # Sends a message in the ecosystem
    def send_message(self, message):
        print("sending: " + message)
#         if self.connect_to_ecosystem:
#             self.mqtt.send(self.mqtt.client_id + "$$$" + message)

    def OSCMessage(self, topic, dataTypes, output):
        global lightOn
        global noise
#         print(topic)
#         print(dataTypes)
#         print(output)
        if topic == "/reefcontrol/timeofday":
            # Update the time of day
            self.creature.time_of_day = int(output[0])
            print("Updated time of day " + str(self.creature.time_of_day))
        if topic == "/reefcontrol/energy":
            # Update the time of day
            self.creature.energy = int(output[0])

    # Checks if there is a message from the eco system
    def check_for_messages(self):
        global offline_messages, offline_timer
        if self.connect_to_ecosystem:
            self.OSCCommunicator.loop(self.creature.OSCMessage)
        else:
            # fake the ecosystem
            if offline_timer.expired():
                offline_timer.set_duration(random.randint(3,8))
                offline_timer.start()
                self.creature.message("reefcontrol/timeofday", random.choice(offline_messages))





