from components.button import Button
from components.buzzer import Buzzer
from components.neopixel_led import NeopixelLED
from components.vibration_motor import VibrationMotor
from components.servo_motor import Servo
from timer import Timer
import time
from varspeed import Vspeed
from behaviours import Behaviours
import random

button = Button()
buzzer = Buzzer()
motor = VibrationMotor()
led = NeopixelLED(1)
servo = Servo()
behaviours = Behaviours()

increase = True
led_power = 255
color = (1, 0, 0, 0)

MIN = 0
MAX = 2 ** 16
vs1 = Vspeed(init_position=0, result="int")
vs1.set_bounds(lower_bound=MIN, upper_bound=MAX)
vs2 = Vspeed(init_position=0, result="int")
vs2.set_bounds(lower_bound=MIN, upper_bound=MAX)


class Creature:
    state_day_nobody = 0
    state_day_somebody = 1
    state_night_nobody = 2
    state_night_somebody = 3
    state_beautiful = 4

    beautiful_duration = 30
    presence_duration = 5
    presence_timer = Timer(beautiful_duration)
    time_of_day = 0
    energy = 0


    current_state = state_day_nobody

    def __init__(self):
        self.ecosystem = None

    def message(self, topic, msg):
        global color
        print("recieved: Topic:" + str(topic) + " Message:" + str(msg))

        # If we receive a new time of day
        if topic == "reefcontrol/timeofday":
            # Update the time of day
            self.time_of_day = int(msg)
#             print("Updated time of day " + str(self.time_of_day))
        if topic == "reefcontrol/energy":
            # Update the time of day
            self.energy = int(msg)

    def sense(self):
        if button.sense() == True:
            return True


    def checkState(self, isRunning):
        if self.current_state == self.state_day_nobody:
            if self.sense():
                self.current_state = self.state_day_somebody
                self.presence_timer.set_duration(self.presence_duration)
                self.presence_timer.start()
            elif self.time_of_day < 360 or self.time_of_day > 1080:
                self.current_state = self.state_night_nobody
            elif self.presence_timer.expired():
                self.current_state = self.state_beautiful

        elif self.current_state == self.state_day_somebody:
            if self.sense():
                self.presence_timer.start()
            elif self.time_of_day < 360 or self.time_of_day > 1080:
                self.current_state = self.state_night_somebody
            elif self.presence_timer.expired():
                self.current_state = self.state_day_nobody
                self.presence_timer.set_duration(self.beautiful_duration)
                self.presence_timer.start()

        elif self.current_state == self.state_night_nobody:
            if self.sense():
                self.current_state = self.state_night_somebody
                self.presence_timer.set_duration(self.presence_duration)
                self.presence_timer.start()
            elif self.time_of_day > 360 and self.time_of_day < 1080:
                self.current_state = self.state_day_nobody
                self.presence_timer.set_duration(self.beautiful_duration)
                self.presence_timer.start()

        elif self.current_state == self.state_night_somebody:
            if self.sense():
                self.presence_timer.start()
            elif self.time_of_day > 360 and self.time_of_day < 1080:
                self.current_state = self.state_day_somebody
                self.presence_timer.set_duration(self.presence_duration)
                self.presence_timer.start()
            elif self.presence_timer.expired():
                self.current_state = self.state_night_nobody


        elif self.current_state == self.state_beautiful:
            if not isRunning:
                self.current_state = self.state_day_nobody
                self.presence_timer.set_duration(self.beautiful_duration)
                self.presence_timer.start()


    # One iteration of the creatures main loop
    def loop(self):
        beh = behaviours.getBehaviour(self.current_state)
        position1, running1, changed1 = vs1.sequence(beh[0], beh[1])
        position2, running2, changed2 = vs2.sequence(beh[2], beh[3])
        self.checkState(running1 or running2)
        print(self.current_state)
        ############################################################
        # Use these variables to do the outputs


        motor.update(position1)
        servo.update(position2)


