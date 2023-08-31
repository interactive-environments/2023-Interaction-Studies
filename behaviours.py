class Behaviours:
    state_day_nobody = 0
    state_day_somebody = 1
    state_night_nobody = 2
    state_night_somebody = 3
    state_beautiful = 4
    def getBehaviour1(self, state):
#         state = self.state_beautiful # Change this to the state you want to test
        if state == self.state_day_nobody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, state)
        if state == self.state_day_somebody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, state)
        if state == self.state_night_nobody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, state)
        if state == self.state_night_somebody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, state)
        if state == self.state_beautiful:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, state)
            
            
            
    
    def getBehaviour2(self, state):
#         state = self.state_beautiful # Change this to the state you want to test
        if state == self.state_day_nobody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, loops)
        if state == self.state_day_somebody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, loops)
        if state == self.state_night_nobody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, loops)
        if state == self.state_night_somebody:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, loops)
        if state == self.state_beautiful:
            sequence = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops = 0
            return (sequence, loops)