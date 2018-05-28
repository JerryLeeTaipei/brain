import iot
import sys, termios, tty, os, time


button_delay = 0.2

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1) 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


        
# test
stop = 0
try:
    mesgServer = iot.iot_mesgServer()
    mesgServer.start()
    while True:
        char = getch()
        if (char == "q"):
            print("Stop!")
            stop = 1
            break
        elif  (char == "c"):
            print("Start client device")
            mesgClient = iot.iot_mesgClient()
            mesgClient.connect()
        else:
            print("Unknown key(%c)\n", chr(char) )
        time.sleep(button_delay) 
except NameError:    
    print("Failed to connect the mesgServer\n")
    raise

if ( stop == 1 ):
    print("User stop\n")
    # stop server
    mesgServer.stop()
else:
    print("Exception? stop\n");

print("Bye\n")
