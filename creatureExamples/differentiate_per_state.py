if self.current_state == self.state_day_nobody:
	led.update_full_color((position1, int(position1/5),int(position1/5)))

elif self.current_state == self.state_day_somebody
	led.update_full_color((int(position1*0.54), 0, 0))
	motor.update(position2) 

elif self.current_state == self.state_night_nobody
	led.update_full_color((0,int(position1 * 0.74), int(position1*0.6)))
	
elif self.current_state == self.state_night_somebod
	led.update_full_color((0,0,int(position1*0.74)))
	motor.update(position2)

elif self.current_state == self.state_beautiful:
	led.update_full_color((int(position1/2), int(position1/3),int(position1/3)))