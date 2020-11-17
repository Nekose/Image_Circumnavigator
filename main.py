from src.interface import user_interface
import sys, os
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys.executable[:-5]
    config_file = os.path.join(application_path, "configuration", "config.txt")
    input_path = os.path.join(application_path, "input")
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(application_path, "data", "configuration", "config.txt")
    input_path = os.path.join(application_path, "data", "input")


with open(config_file) as file:
    config_options = file.readlines()
    config_dict = {}
    for element in config_options:
        element = element.split("=")
        config_dict[element[0].strip()] = element[1].strip()
user_interface(input_path, config_dict['output_path'])