from phue import Bridge
import time

b = Bridge('') # b = Bridge('ip_of_your_bridge')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
# b.connect()

lights = [11, 12] # Use lights you'd prefer to use


def convertColor(hexCode):
    R = int(hexCode[:2], 16)
    G = int(hexCode[2:4], 16)
    B = int(hexCode[4:6], 16)

    total = R + G + B

    if R == 0:
        firstPos = 0
    else:
        firstPos = R / total

    if G == 0:
        secondPos = 0
    else:
        secondPos = G / total

    return [firstPos, secondPos]

def flash(colour):
    b.set_light(lights, {'on' : True, 'bri' : 254, 'xy' : convertColor(colour)})
    time.sleep(0.7)
    b.set_light(lights, 'on', False)

flash('ff361f') # red
flash('fefe00') # yellow
flash('04ff02') # green



