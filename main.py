def on_logo_released():
    wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 90)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

def on_button_pressed_ab():
    wuKong.stop_all_motor()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_logo_touched():
    global angulo
    angulo = 160
    wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, angulo)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

angulo = 0
wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 90)
for index in range(4):
    wuKong.set_motor_speed(wuKong.MotorList.M1, 16)
    basic.pause(50)
    wuKong.set_motor_speed(wuKong.MotorList.M1, 0)

def on_forever():
    while input.button_is_pressed(Button.A):
        wuKong.set_motor_speed(wuKong.MotorList.M1, -13)
        basic.pause(200)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 0)
basic.forever(on_forever)

def on_forever2():
    while input.button_is_pressed(Button.A) and input.logo_is_pressed():
        wuKong.set_motor_speed(wuKong.MotorList.M2, -42)
        basic.pause(100)
        wuKong.set_motor_speed(wuKong.MotorList.M2, 0)
basic.forever(on_forever2)

def on_forever3():
    while input.button_is_pressed(Button.B):
        wuKong.set_motor_speed(wuKong.MotorList.M2, -40)
        basic.pause(100)
        wuKong.set_motor_speed(wuKong.MotorList.M2, 0)
basic.forever(on_forever3)

def on_forever4():
    while input.button_is_pressed(Button.B) and input.logo_is_pressed():
        wuKong.set_motor_speed(wuKong.MotorList.M2, 40)
        basic.pause(100)
        wuKong.set_motor_speed(wuKong.MotorList.M2, 0)
basic.forever(on_forever4)
