from phue import Bridge
import time

b = Bridge('ip_of_your_bridge') # b = Bridge('ip_of_your_bridge')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
# b.connect()

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



b.set_light([11, 12],'on', True)
b.set_light([11, 12], 'bri', 254)

b.set_light([11, 12],'xy',convertColor('FF0000'))
time.sleep(2)
b.set_light([11, 12],'xy',convertColor('1FC600'))
time.sleep(2)

b.set_light([11, 12],'on', False)