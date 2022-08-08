#create a new project at: https://makecode.microbit.org/#editor
# drop the code below into the edtor - and then download the .hex code it produceds

def on_forever():
    temp1=input.temperature()*9/5+32
    basic.pause(3000)
    basic.show_string(str(temp1) + 'F')
    serial.write_line(str(temp1))

basic.forever(on_forever)
