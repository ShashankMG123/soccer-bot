import wiringpi as wp
wp.wiringPiSetupGpio()

def Motor(x,y,pwm):
	wp.pinMode(x,1)
	wp.pinMode(y,1)
	wp.pinMode(pwm,1)
	wp.softPwmCreate(pwm,0,100)
	return x,y,pwm
def forward(motor,speed):
	(x,y,pwm)= motor
	wp.digitalWrite(x,0)
	wp.digitalWrite(y,1)
	wp.softPwmWrite(pwm,speed)
def backward(motor,speed):
	(x,y,pwm)=motor
	wp.digitalWrite(x,1)
	wp.digitalWrite(y,0)
	wp.softPwmWrite(pwm,speed)

motor1= Motor(23,24,25) #connect motor 1 to pin 23,24
motor2= Motor(20,21,26) #connet morot 2 to pin 20 ,21
forward(motor1,40)
backward(motor2,40)
wp.delay(2200)
forward(motor1,0)
forward(motor2,0)
wp.delay(100)
forward(motor1,40)
forward(motor2,40)
wp.delay(2000)
forward(motor1,0)
forward(motor2,0)
wp.delay(100)
forward(motor1,40)
backward(motor2,40)
wp.delay(2200)
forward(motor1,0)
backward(motor2,0)
