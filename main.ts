input.onLogoEvent(TouchButtonEvent.Released, function () {
    wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 90)
})
input.onButtonPressed(Button.AB, function () {
    wuKong.stopAllMotor()
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    angulo = 160
    wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, angulo)
})
let angulo = 0
wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 90)
for (let index = 0; index < 4; index++) {
    wuKong.setMotorSpeed(wuKong.MotorList.M1, 16)
    basic.pause(50)
    wuKong.setMotorSpeed(wuKong.MotorList.M1, 0)
}
basic.forever(function () {
    while (input.buttonIsPressed(Button.A)) {
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -13)
        basic.pause(200)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 0)
    }
})
basic.forever(function () {
    while (input.buttonIsPressed(Button.A) && input.logoIsPressed()) {
        wuKong.setMotorSpeed(wuKong.MotorList.M2, -42)
        basic.pause(100)
        wuKong.setMotorSpeed(wuKong.MotorList.M2, 0)
    }
})
basic.forever(function () {
    while (input.buttonIsPressed(Button.B)) {
        wuKong.setMotorSpeed(wuKong.MotorList.M2, -40)
        basic.pause(100)
        wuKong.setMotorSpeed(wuKong.MotorList.M2, 0)
    }
})
basic.forever(function () {
    while (input.buttonIsPressed(Button.B) && input.logoIsPressed()) {
        wuKong.setMotorSpeed(wuKong.MotorList.M2, 40)
        basic.pause(100)
        wuKong.setMotorSpeed(wuKong.MotorList.M2, 0)
    }
})
