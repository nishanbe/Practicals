"""
Write Python for a program that opens a file and toggles "on" and "off" each time it's run.
So, if the file contains "on", change it to "off" and vice versa
"""
try:
    in_file = open("switch.txt", "r")
    text = in_file.read()
    in_file = open("switch.txt", "w")
    if text == "OFF":
        in_file.write("ON")
        print("Changed to ON")
    else:
        in_file.write("OFF")
        print("Changed to OFF")
    in_file.close()
except FileNotFoundError:
    in_file = open("switch.txt", "w")
    in_file.write("ON")
    print("File created and 'ON' is written into it.")
    in_file.close()