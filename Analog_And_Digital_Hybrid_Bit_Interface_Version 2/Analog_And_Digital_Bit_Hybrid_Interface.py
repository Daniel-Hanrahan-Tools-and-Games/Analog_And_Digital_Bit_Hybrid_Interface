from time import sleep
import time
import glob, os
import psutil
import lupa

# mod prompt is up here so it can be global
strModPrompt = input("Do you want to use mods, y = yes, n = no: ");
if strModPrompt == "y":
    
    # library for mods and process vm call needed for mods
    from lupa import LuaRuntime
    lua = LuaRuntime()

    # The mod file must be in your home directory and must be called note_data_to_instrument_mod.lua
    lua.execute(r'''dofile("Analog_And_Digital_Hybrid_Bit_Interface_Mod.lua")''')
    
    # get the mod global envirorment
    globals = lua.globals()

    # Mod Notice and Name
    strModNoticeAndName = lua.globals().strNoticeAndName
    print("You are using a mod: \n")
    print(strModNoticeAndName)

if strModPrompt == "n":
    print("You decided not to use a mod")

# menu function
def menu():
    # new line to seperate instances
    # Copyright and license notice
    print("\n");
    print("Copyright (C) 2022-2023 Daniel Hanrahan");
    print("\n");
    print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU");
    print("General Public License as published by the Free Software Foundation, either version 3 of the License, or");
    print("(at your option) any later version.");
    print("\n");
    print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without");
    print("even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.");
    print("See the GNU General Public License for more details.");
    print("\n");
    print("You should have received a copy of the GNU General Public License along with this program. If not, see");
    print("<https://www.gnu.org/licenses/>.");
    print("\n");
    
    intBits = 3;
    intDigitalStates = (intBits * intBits) - 1;
    print("The amt of possible digital states with the optical ram is: \n", intDigitalStates);
    intCPUCores = os.cpu_count()
    dblClockSpeed = psutil.cpu_freq()
    dblPossibleAnalogStates = (intCPUCores * dblClockSpeed) * intBits;
    print("The amt of possible analog states this machine has is \n", dblPossibleAnalogStates)
    
   
    # type in for what device you want to use and notice for exiting
    strDirectory = input(" What device do you want to use Raspberry Pi (0), Arduino(1) or exit out of the app(exit):");
    # What heppens when Raspberry Pi is chosen
    if strDirectory == "0":
        # Goes to Raspberry Pi function
        RaspberryPi()
    
    # What happens when Arduino is chosen
    elif strDirectory == "1":
        # Goes to Arduino function
        Arduino()
        
    # exit command    
    elif strDirectory == "exit":
        print("Good Bye")
        exit();
        
    # validation    
    else:
        print("Good Bye")
        exit();

# Arduino function
def Arduino():
    # input for Bit 0 mode
    strBit0Mode = input(" What mode do you want for bit 0, Analog(0) or Digital(1):");
    # if digital is selected for bit 0 it goes to the digital bit 0 function
    if strBit0Mode == "1":
        # makes sure analog was not selected
        dblAnalogBit0 = 0;
        # goes to digital bit 0 function for Arduino
        intBit0 = ArduinoDigitalBit0();
    # if analog is selected for bit 0 it goes to the analog bit 0 function
    elif strBit0Mode == "0":
        # makes sure digital bit was not selected
        intBit0 = 0;
        # goes to analog bit 0 function for Arduino
        dblAnalogBit0 = ArduinoAnalogBit0();
    # validation    
    else:
        print("Good Bye")
        exit();
        
    # input for Bit 1 mode
    strBit1Mode = input(" What mode do you want for bit 1, Analog(0) or Digital(1):");
    # if digital is selected for bit 0 it goes to the digital bit 0 function
    if strBit1Mode == "1":
        # makes sure analog was not selected
        dblAnalogBit1 = 0;
        # goes to digital bit 0 function for Arduino
        intBit1 = ArduinoDigitalBit1();
    # if analog is selected for bit 0 it goes to the analog bit 0 function
    elif strBit1Mode == "0":
        # makes sure digital bit was not selected
        intBit1 = 0;
        # goes to analog bit 0 function for Arduino
        dblAnalogBit1 = ArduinoAnalogBit1();
    # validation    
    else:
        print("Good Bye")
        exit();
        
    # input for Bit 2 mode
    strBit2Mode = input(" What mode do you want for bit 2, Analog(0) or Digital(1):");
    # if digital is selected for bit 2 it goes to the digital bit 2 function
    if strBit2Mode == "1":
        # makes sure analog was not selected
        dblAnalogBit2 = 0;
        # goes to digital bit 0 function for Arduino
        intBit2 = ArduinoDigitalBit2();
    # if analog is selected for bit 2 it goes to the analog bit 2 function
    elif strBit2Mode == "0":
        # makes sure digital bit was not selected
        intBit2 = 0;
        # goes to analog bit 0 function for Arduino
        dblAnalogBit2 = ArduinoAnalogBit2();
    # validation    
    else:
        print("Good Bye")
        exit();
        
    # calculates the ram state
    dblDigitalStates = int(intBit0) + int(intBit1) + int(intBit2);
    dblAnalogStates = dblAnalogBit0 + dblAnalogBit1 + dblAnalogBit2;
    dblRamState = dblDigitalStates + dblAnalogStates;
    # displays the state of ram
    print("\n")
    print("\n")
    print("\n")
    print ("Ram State: ")
    print(dblRamState)
    print("\n")
    print("\n")
    print("\n")
    
    # goes back to the menu
    return menu();
        
# Arduino digital bit 0 function
def ArduinoDigitalBit0():
    # calls usb ports
    import serial

    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks user what value it wants for this bit
    strBitState = input(" What state do you want for bit 0, 0 or 1:");
    # What happens when user says 1 state
    if strBitState == "1":
        arduinoDriver.write(b'a')
    # What happens when user says 0 state
    elif strBitState == "0":
        arduinoDriver.write(b'b')
    #needed to reliably read the data
    sleep(1)
    # checks for data
    while True:
        # Reads line from arduino
        value = arduinoDriver.readline()[:-2]
        # decodes values from bytes
        value = value.decode()
        value = value.replace(".", "")
        value = float(value)
        # 2nd check for data
        if value:
            # Test
            print("Test Case:")
            print(value)
            
            # a 2nd big source of light is needed to reliably read the data
            # these values for 0 and 1 may need to be fine tuned to your set up
            if (value >= 44):
                print("1");
                # returns state of intBit0 to the menu so the user knows what state the ram is in
                intBit0 = 1;
                if strModPrompt == "y":
                    # output for mod
                    ModOutput = globals.Dbit0State1()
                    print(ModOutput)
                return int(intBit0);
            elif (value == 0):
                print("0");
                # returns state of intBit0 to the menu so the user knows what state the ram is in
                intBit0 = 0;
                if strModPrompt == "y":
                    # output for mod
                    ModOutput = globals.Dbit0State0()
                    print(ModOutput)
                return int(intBit0);
        
# Arduino analog bit 0 function
def ArduinoAnalogBit0():
    # calls usb ports
    import serial

    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks user what value it wants for this bit
    dblBitState = float(input("What state do you want for bit 0, it needs to be a number between 0 and 100, 0 is the lowest and 100 is the highest: "));
    # validation for analog bit
    if dblBitState < 0 and dblBitState > 100:
        print("Needs to be greater than 0 and less than 100")
        return ArduinoAnalogBit0;
    # tells arduino that bit 0 is analog
    arduinoDriver.write(b'g')
    # determines the state of the bit
    dblBitState = float(dblBitState)
    dblBitState = str(dblBitState)
    arduinoDriver.write(dblBitState.encode())
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()
    value = value.replace(".", "")
    value = float(value)
    # test case
    print("Test Case: ")
    print(value / 1023.0 * 3.3)

    # a 2nd big source of light is needed to reliably read the data
    # the hard value in dblValue2 may need to be fine tuned to your set up
    # Validation for 0s
    if value == 0:
        dblValue4 = 0;
    else:
        dblValue = value / 1023.0 * 3.3
        dblValue2 = dblValue - 0.0032258064516129032
        dblValue3 = (dblValue2 / dblValue) * 100
        dblValue4 = (dblValue3 / 100) * 1
        
    if strModPrompt == "y":
        # output for mod
        ModOutput = globals.Abit0(dblValue4)
        print(ModOutput)

    print(dblValue4)
    return dblValue4;

# Arduino digital bit 1 function
def ArduinoDigitalBit1():
    # calls usb ports
    import serial

    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks user what value it wants for this bit
    strBitState = input(" What state do you want for bit 1, 0 or 1:");
    # What happens when user says 1 state
    if strBitState == "1":
        arduinoDriver.write(b'c')
    # What happens when user says 0 state
    elif strBitState == "0":
        arduinoDriver.write(b'd')
    #needed to reliably read the data
    sleep(1)
    # checks for data
    while True:
        # Reads line from arduino
        value = arduinoDriver.readline()[:-2]
        # decodes values from bytes
        value = value.decode()
        value = value.replace(".", "")
        value = float(value)
        # 2nd check for data
        if value:
            # Test
            print("Test Case:")
            print(value)
            
            # a 2nd big source of light is needed to reliably read the data
            # these values for 0 and 1 may need to be fine tuned to your set up
            if (value >= 44):
                print("1");
                # returns state of intBit1 to the menu so the user knows what state the ram is in
                intBit1 = 2;
                if strModPrompt == "y":
                    # output for mod
                    ModOutput = globals.Dbit1State1()
                    print(ModOutput)
                return int(intBit1);
            elif (value == 0):
                print("0");
                # returns state of intBit1 to the menu so the user knows what state the ram is in
                intBit1 = 0;
                if strModPrompt == "y":
                    # output for mod
                    ModOutput = globals.Dbit1State0()
                    print(ModOutput)
                return int(intBit1);
        
# Arduino analog bit 1 function
def ArduinoAnalogBit1():
    # calls usb ports
    import serial

    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks user what value it wants for this bit
    dblBitState = float(input("What state do you want for bit 1, it needs to be a number between 0 and 100, 0 is the lowest and 100 is the highest: "));
    # validation for analog bit
    if dblBitState < 0 and dblBitState > 100:
        print("Needs to be greater than 0 and less than 100")
        return ArduinoAnalogBit1;
    # tells arduino that bit 1 is analog
    arduinoDriver.write(b'h')
    # determines the state of the bit
    dblBitState = float(dblBitState)
    dblBitState = str(dblBitState)
    arduinoDriver.write(dblBitState.encode())
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()
    value = value.replace(".", "")
    value = float(value)
    # test case
    print("Test Case: ")
    print(value / 1023.0 * 3.3)

    # a 2nd big source of light is needed to reliably read the data
    # the hard value in dblValue2 may need to be fine tuned to your set up
    # Validation for 0s
    if value == 0:
        dblValue4 = 0;
    else:
        dblValue = value / 1023.0 * 3.3
        dblValue2 = dblValue - 0.0032258064516129032
        dblValue3 = (dblValue2 / dblValue) * 100
        dblValue4 = (dblValue3 / 100) * 2
        
    if strModPrompt == "y":
        # output for mod
        ModOutput = globals.Abit1(dblValue4)
        print(ModOutput)
        
    print(dblValue4)
    return dblValue4;

# Arduino digital bit 2 function
def ArduinoDigitalBit2():
    # calls usb ports
    import serial

    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks user what value it wants for this bit
    strBitState = input(" What state do you want for bit 2, 0 or 1:");
    # What happens when user says 1 state
    if strBitState == "1":
        arduinoDriver.write(b'e')
    # What happens when user says 0 state
    elif strBitState == "0":
        arduinoDriver.write(b'f')
    #needed to reliably read the data
    sleep(1)
    # checks for data
    while True:
        # Reads line from arduino
        value = arduinoDriver.readline()[:-2]
        # decodes values from bytes
        value = value.decode()
        value = value.replace(".", "")
        value = float(value)
        # 2nd check for data
        if value:
            # Test
            print("Test Case:")
            print(value)
            
            # a 2nd big source of light is needed to reliably read the data
            # these values for 0 and 1 may need to be fine tuned to your set up
            if (value >= 44):
                print("1");
                # returns state of intBit2 to the menu so the user knows what state the ram is in
                intBit2 = 4;
                if strModPrompt == "y":
                    # output for mod
                    ModOutput = globals.Dbit2State1()
                    print(ModOutput)
                return int(intBit2);
            elif (value == 0):
                print("0");
                # returns state of intBit2 to the menu so the user knows what state the ram is in
                intBit2 = 0;
                if strModPrompt == "y":
                    # output for mod
                    ModOutput = globals.Dbit2State0()
                    print(ModOutput)
                return int(intBit2);
        
# Arduino analog bit 2 function
def ArduinoAnalogBit2():
    # calls usb ports
    import serial

    # asks for the port for arduino
    arduinoDriverPort = input("What is the port for the arduino (case sensitive): ")
    print("\n");

    # calls the Arduino druver
    arduinoDriver = serial.Serial(arduinoDriverPort, baudrate = 57600, timeout=.1)
    
    # asks user what value it wants for this bit
    dblBitState = float(input("What state do you want for bit 2, it needs to be a number between 0 and 100, 0 is the lowest and 100 is the highest: "));
    # validation for analog bit
    if dblBitState < 0 and dblBitState > 100:
        print("Needs to be greater than 0 and less than 100")
        return ArduinoAnalogBit2;
    # tells arduino that bit 2 is analog
    arduinoDriver.write(b'i')
    # determines the state of the bit
    dblBitState = float(dblBitState)
    dblBitState = str(dblBitState)
    arduinoDriver.write(dblBitState.encode())
    #needed to reliably read the data
    sleep(1)
    # Reads Line from Arduino
    value = arduinoDriver.readline()[:-2]
    # decodes values from bytes
    value = value.decode()
    value = value.replace(".", "")
    value = float(value)
    # test case
    print("Test Case: ")
    print(value / 1023.0 * 3.3)

    # a 2nd big source of light is needed to reliably read the data
    # the hard value in dblValue2 may need to be fine tuned to your set up
    # Validation for 0s
    if value == 0:
        dblValue4 = 0;
    else:
        dblValue = value / 1023.0 * 3.3
        dblValue2 = dblValue - 0.0032258064516129032
        dblValue3 = (dblValue2 / dblValue) * 100
        dblValue4 = (dblValue3 / 100) * 4

    if strModPrompt == "y":
        # output for mod
        ModOutput = globals.Abit2(dblValue4)
        print(ModOutput)

    print(dblValue4)
    return dblValue4;
    
# Raspberry Pi function
def RaspberryPi():
    #spi must be enabled in raspi-config

    # input for Bit 0 mode
    strBit0Mode = input(" What mode do you want for bit 0, Analog(0) or Digital(1):");
    # if digital is selected for bit 0 it goes to the digital bit 0 function
    if strBit0Mode == "1":
        # makes sure analog was not selected
        dblAnalogBit0 = 0;
        # goes to digital bit 0 function for Raspberry Pi
        intBit0 = piDigitalBit0();
    # if analog is selected for bit 0 it goes to the analog bit 0 function
    elif strBit0Mode == "0":
        # makes sure digital bit was not selected
        intBit0 = 0;
        # goes to analog bit 0 function for Raspberry Pi
        dblAnalogBit0 = piAnalogBit0();
    # validation    
    else:
        print("Good Bye")
        exit();
    
    # input for Bit 1 mode
    strBit1Mode = input(" What mode do you want for bit 1, Analog(0) or Digital(1):");
    # if digital is selected for bit 1 it goes to the digital bit 1 function
    if strBit1Mode == "1":
        # makes sure analog was not selected
        dblAnalogBit1 = 0;
        # goes to digital bit 1 function for Raspberry Pi
        intBit1 = piDigitalBit1();
    # if analog is selected for bit 1 it goes to the analog bit 1 function
    elif strBit1Mode == "0":
        # makes sure digital bit was not selected
        intBit1 = 0;
        # goes to analog bit 1 function for Raspberry Pi
        dblAnalogBit1 = piAnalogBit1();
    # validation    
    else:
        print("Good Bye")
        exit();
    
    # input for Bit 2 mode
    strBit2Mode = input(" What mode do you want for bit 2, Analog(0) or Digital(1):");
    # if digital is selected for bit 2 it goes to the digital bit 2 function
    if strBit2Mode == "1":
        # makes sure analog was not selected
        dblAnalogBit2 = 0;
        # goes to digital bit 2 function for Raspberry Pi
        intBit2 = piDigitalBit2();
    # if analog is selected for bit 2 it goes to the analog bit 2 function
    elif strBit2Mode == "0":
        # makes sure digital bit was not selected
        intBit2 = 0;
        # goes to analog bit 2 function for Raspberry Pi
        dblAnalogBit2 = piAnalogBit2();
    # validation    
    else:
        print("Good Bye")
        exit();
    
    # calculates the ram state
    dblDigitalStates = int(intBit0) + int(intBit1) + int(intBit2);
    dblAnalogStates = dblAnalogBit0 + dblAnalogBit1 + dblAnalogBit2;
    dblRamState = dblDigitalStates + dblAnalogStates;
    # displays the state of ram
    print("\n")
    print("\n")
    print("\n")
    print ("Ram State: ")
    print(dblRamState)
    print("\n")
    print("\n")
    print("\n")
    
    # goes back to the menu
    return menu();

# Raspberry Pi digital bit 0 function
def piDigitalBit0():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.OUT)
    
    # asks user what value it wants for this bit
    strBitState = input(" What state do you want for bit 0, 0 or 1:");
    # What happens when user says 1 state
    if strBitState == "1":
        GPIO.output(3, GPIO.HIGH)
    # What happens when user says 0 state
    elif strBitState == "0":
        GPIO.output(3, GPIO.LOW)
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 2 of the ADC
    value = adc.read2( channel = 2 )
    # Test
    print("Test Case:")
    print(value)
    
    # a 2nd big source of light is needed to reliably read the data
    # these values for 0 and 1 may need to be fine tuned to your set up
    if (value >= 44):
        print("1");
        # returns state of intBit0 to the menu so the user knows what state the ram is in
        intBit0 = 1;
        if strModPrompt == "y":
            # output for mod
            ModOutput = globals.Dbit0State1()
            print(ModOutput)
        return int(intBit0);
    elif (value == 0):
        print("0");
        # returns state of intBit0 to the menu so the user knows what state the ram is in
        intBit0 = 0;
        if strModPrompt == "y":
            # output for mod
            ModOutput = globals.Dbit0State0()
            print(ModOutput)
        return int(intBit0);
        
# Raspberry Pi analog bit 0 function
def piAnalogBit0():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.OUT)
    
    pwm = GPIO.PWM(3, 50)
    pwm.start(0)
    # asks user what value it wants for this bit
    dblBitState = float(input("What state do you want for bit 0, it needs to be a number between 0 and 100, 0 is the lowest and 100 is the highest: "));
    # validation for analog bit
    if dblBitState < 0 and dblBitState > 100:
        print("Needs to be greater than 0 and less than 100")
        return piAnalogBit0;

    # determines the state of the bit
    dblBitState = float(dblBitState)
    pwm.ChangeDutyCycle(dblBitState)
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 2 of the ADC
    value = adc.read2( channel = 2 )
    # test case
    print("Test Case: ")
    print(value / 1023.0 * 3.3)

    # a 2nd big source of light is needed to reliably read the data
    # the hard value in dblValue2 may need to be fine tuned to your set up
    # Validation for 0s
    if value == 0:
        dblValue4 = 0;
    else:
        dblValue = value / 1023.0 * 3.3
        dblValue2 = dblValue - 0.0032258064516129032
        dblValue3 = (dblValue2 / dblValue) * 100
        dblValue4 = (dblValue3 / 100) * 1

    if strModPrompt == "y":
        # output for mod
        ModOutput = globals.Abit0(dblValue4)
        print(ModOutput)

    print(dblValue4)
    return dblValue4;
    
# Raspberry Pi digital bit 1 function
def piDigitalBit1():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    
    # asks user what value it wants for this bit
    strBitState = input(" What state do you want for bit 1, 0 or 1:");
    # What happens when user says 1 state
    if strBitState == "1":
        GPIO.output(4, GPIO.HIGH)
    # What happens when user says 0 state
    elif strBitState == "0":
        GPIO.output(4, GPIO.LOW)
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 1 of the ADC
    value = adc.read1( channel = 1 )
    # Test
    print("Test Case:")
    print(value)
    
    # a 2nd big source of light is needed to reliably read the data
    # these values for 0 and 1 may need to be fine tuned to your set up
    if (value >= 635):
        print("1");
        # returns state of intBit1 to the menu so the user knows what state the ram is in
        intBit1 = 2;
        if strModPrompt == "y":
            # output for mod
            ModOutput = globals.Dbit1State1()
            print(ModOutput)
        return int(intBit1);
    elif (value <= 71):
        print("0");
        # returns state of intBit1 to the menu so the user knows what state the ram is in
        intBit1 = 0;
        if strModPrompt == "y":
            # output for mod
            ModOutput = globals.Dbit1State0()
            print(ModOutput)
        return int(intBit1);
        
# Raspberry Pi analog bit 1 function
def piAnalogBit1():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    
    pwm = GPIO.PWM(4, 50)
    pwm.start(0)
    # asks user what value it wants for this bit
    dblBitState = float(input("What state do you want for bit 1, it needs to be a number between 0 and 100, 0 is the lowest and 100 is the highest: "));
    # validation for analog bit
    if dblBitState < 0 and dblBitState > 100:
        print("Needs to be greater than 0 and less than 100")
        return piAnalogBit1;

    # determines the state of the bit
    dblBitState = float(dblBitState)
    pwm.ChangeDutyCycle(dblBitState)
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 1 of the ADC
    value = adc.read1( channel = 1 )
    # test case
    print("Test Case: ")
    print(value / 1023.0 * 3.3)

    # a 2nd big source of light is needed to reliably read the data
    # the hard value in dblValue2 may need to be fine tuned to your set up
    # Validation for 0s
    if value == 0:
        dblValue4 = 0;
    else:
        dblValue = value / 1023.0 * 3.3
        dblValue2 = dblValue
        dblValue3 = dblValue * 100
        dblValue4 = (dblValue3 / 100) * 2

    if strModPrompt == "y":
        # output for mod
        ModOutput = globals.Abit0(dblValue4)
        print(ModOutput)

    print(dblValue4)
    return dblValue4;
    
# Raspberry Pi digital bit 2 function
def piDigitalBit2():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    
    # asks user what value it wants for this bit
    strBitState = input(" What state do you want for bit 2, 0 or 1:");
    # What happens when user says 1 state
    if strBitState == "1":
        GPIO.output(2, GPIO.HIGH)
    # What happens when user says 0 state
    elif strBitState == "0":
        GPIO.output(2, GPIO.LOW)
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 0 of the ADC
    value = adc.read0( channel = 0 )
    # Test
    print("Test Case:")
    print(value)
    
    # a 2nd big source of light is needed to reliably read the data
    # these values for 0 and 1 may need to be fine tuned to your set up
    if (value >= 635):
        print("1");
        # returns state of intBit2 to the menu so the user knows what state the ram is in
        intBit2 = 4;
        if strModPrompt == "y":
            # output for mod
            ModOutput = globals.Dbit2State1()
            print(ModOutput)
        return int(intBit2);
    elif (value <= 71):
        print("0");
        # returns state of intBit2 to the menu so the user knows what state the ram is in
        intBit2 = 0;
        if strModPrompt == "y":
            # output for mod
            ModOutput = globals.Dbit2State0()
            print(ModOutput)
        return int(intBit2);
        
# Raspberry Pi analog bit 2 function
def piAnalogBit2():
    # calls gpio module
    import RPi.GPIO as GPIO
    # calls analog to digital converter driver
    from Raspberry_Pi_ADC_Driver import MCP3008
    
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    
    pwm = GPIO.PWM(2, 50)
    pwm.start(0)
    # asks user what value it wants for this bit
    dblBitState = float(input("What state do you want for bit 2, it needs to be a number between 0 and 100, 0 is the lowest and 100 is the highest: "));
    # validation for analog bit
    if dblBitState < 0 and dblBitState > 100:
        print("Needs to be greater than 0 and less than 100")
        return piAnalogBit2;

    # determines the state of the bit
    dblBitState = float(dblBitState)
    pwm.ChangeDutyCycle(dblBitState)
    # tells driver what ADC it is using
    adc = MCP3008()
    #needed to reliably read the data
    sleep(1)
    # Reads from channel 0 of the ADC
    value = adc.read0( channel = 0 )
    # test case
    print("Test Case: ")
    print(value / 1023.0 * 3.3)

    # a 2nd big source of light is needed to reliably read the data
    # the hard value in dblValue2 may need to be fine tuned to your set up
    # Validation for 0s
    if value == 0:
        dblValue4 = 0;
    else:
        dblValue = value / 1023.0 * 3.3
        dblValue2 = dblValue
        dblValue3 = dblValue * 100
        dblValue4 = (dblValue3 / 100) * 4

    if strModPrompt == "y":
        # output for mod
        ModOutput = globals.Abit0(dblValue4)
        print(ModOutput)

    print(dblValue4)
    return dblValue4;

menu();
