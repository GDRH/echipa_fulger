import serial
camera = serial.Serial( "/dev/ttyACM0", 115200 )
mbot = serial.Serial( "/dev/serial0", 115200 )

lights = "\xff\x55\x09\x00\x02\x08\x07\x02\x00\x00\x00\x00"
left = "\xff\x55\x09\x00\x02\x08\x07\x02\x02\xff\x00\x00"
right = "\xff\x55\x09\x00\x02\x08\x07\x02\x01\x00\x00\xff"

mbot.write(lights)

while(1):
    print("-")
    line = camera.readline()
    print("*")
    data = line.split(",")
    print(len(data))
    if(len(data) != 6):
        continue
    width = float(data[0])
    x1 = float(data[1])
    y1 = float(data[2])
    x2 = float(data[3])
    y2 = float(data[4])
    print("line: " + str(width) + " " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
    if (( x2 > width/4 ) and (x2 < 3 * width / 4)):
        if( x1 > 3 * width/4 ):
            # move right    ff 55 07 00 02 05 9c ff 9c ff
            mbot.write("\xff\x55\x07\x00\x02\x05\x9c\xff\x9c\xff")
	    mbot.write(lights)
	    mbot.write(right)
        if( x1 < width/4 ):
            # move left     ff 55 07 00 02 05 64 00 64 00
            mbot.write("\xff\x55\x07\x00\x02\x05\x64\x00\x64\x00")
            mbot.write(lights)
	    mbot.write(left)
	if( (x1 > width/4) and (x1 < 3 * width / 4) ):
            # move forward  ff 55 07 00 02 05 38 ff c8 00
            mbot.write("\xff\x55\x07\x00\x02\x05\x38\xff\xc8\x00")
    elif ( x2 < width/4):
        if ( x1 < 3 * width / 4 ):
            # move left     ff 55 07 00 02 05 32 00 32 00
            mbot.write("\xff\x55\x07\x00\x02\x05\x64\x00\x64\x00")
        else:
            # move forward  ff 55 07 00 02 05 9c ff 64 00
            mbot.write("\xff\x55\x07\x00\x02\x05\x38\xff\xc8\x00")
    elif ( x2 > 3 * width / 4 ):
        if (x1 > width / 4 ):
            # move right   ff 55 07 00 02 05 ce ff ce ff
            mbot.write("\xff\x55\x07\x00\x02\x05\x9c\xff\x9c\xff")
        else:
            # move forward ff 55 07 00 02 05 9c ff 64 00
            mbot.write("\xff\x55\x07\x00\x02\x05\x38\xff\xc8\x00")
