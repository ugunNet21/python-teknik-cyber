pin_length=4
direction=1
# python .\pin_dua.py crack -c .\config_file.py
# Load configuration
def load_config(config_file):
    global PIN_LENGTH
    global DIRECTION

    if not os.path.isfile(config_file):
        print("Configuration file not found:", config_file)
        exit(1)

    with open(config_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=")
                if key == "pin_length":
                    PIN_LENGTH = int(value)
                elif key == "direction":
                    DIRECTION = int(value)
