import serial

ser = serial.Serial('/dev/cu.usbmodem143202', 115200, timeout=None)
while True:
    data_raw = ser.readline()
    # next few lines just clean up the serial data
    tempf = str(data_raw)[:7]
    tempf = tempf.replace("b'", "")
    # print to screen (for now)
    print(tempf)
