class Behaviours:
    state_day_nobody = 0
    state_day_somebody = 1
    state_night_nobody = 2
    state_night_somebody = 3
    state_beautiful = 4
    def getBehaviour(self, state):
#         state = self.state_beautiful # Change this to the state you want to test
        if state == self.state_day_nobody:
            sequence1 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops1 = 0
            sequence2 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_day_somebody:
            sequence1 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops1 = 0
            sequence2 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_night_nobody:
            sequence1 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops1 = 0
            sequence2 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_night_somebody:
            sequence1 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops1 = 0
            sequence2 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_beautiful:
            sequence1 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops1 = 1
            sequence2 = [(90, 2, 10, "QuadEaseIn"),
                   (0, 2.0, 10, "QuadEaseOut"),
                   (180, 2.0, 10, "SineEaseInOut")]
            loops2 = 1
            return (sequence1, loops1, sequence2, loops2)
