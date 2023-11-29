
def sun_angle(time):
 
	hour, minute = time.split(':') # split the time into hour and minute
 
	t_h = int(hour)
 
	t_m = int(minute)
 
	time = t_h +  t_m/60
 
	if((time< 6.00) or (time > 18.00)):
 
		return "I don't see the sun!"
 
	if(t_h < 12):
 
		t_h = (t_h - 6) * 15
 
	else:
 
		t_h = 90 + (t_h - 12) * 15
 
	if(t_m != 0):
 
		t_m = t_m * 15/60
 
		return t_h + t_m
 
	else:
 
		return t_h

# TEST:
def disp(time):
	print("The angle of sun at {} is: {}".format(time, sun_angle(time)))
	
for T in range(4, 24, 2):
	disp(str(T) + ":15")
