import serial
import lewansoul_lx16a
import time

SERIAL_PORT = '/dev/ttyUSB0'

controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200, timeout=1),
)

#assume -120~120 => 0~1000
def ang2Value(angle):
    return int(angle*500.0/120.0 + 500.0)

def val2Angle(val):
    return (float(val)- 500.0)*120.0/500.0  

while True:
    # control servos directly
    ang = -10.0
    val = ang2Value(ang)
    controller.move(3, val, 1000) # move servo ID=1 to position 100
    time.sleep(2)
    pos=controller.get_position(3)
    print(ang, val, pos,  val2Angle(pos))

    ang = 10.0
    val = ang2Value(ang)
    controller.move(3, val, 1000) # move servo ID=1 to position 100
    time.sleep(2)
    pos=controller.get_position(3)
    print(ang, val, pos,  val2Angle(pos))