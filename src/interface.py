import sys, os, time
from src.converter import Converter
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys.executable[:-5]
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

def user_interface(input_path, output_path, logo, log_path):
    with open(logo) as file:
        for line in file:
            print(line.strip("\n"))
    print("\nImage Circumnavigator version 1.1")
    print("By Peter Rucker")
    time.sleep(2)
    os.system('cls')
    return user_menu(input_path,output_path,log_path)

def user_menu(input_path, output_path, log_path):
    menu_choices = []
    for filename in os.listdir(input_path):
        extension = filename.split(".")[-1]
        if extension == "csv" or extension == "xls":
            menu_choices.append(filename)
    for pos,val in enumerate(menu_choices):
        print(f"[{pos}]: {val[0:-4]}")
    valid_input = False
    while valid_input == False:
        user_input = input("\nPlease select a number from the choices listed above, or Q to exit: \n")
        if user_input == "Q" or user_input == "q":
            sys.exit()
        if not user_input.isnumeric():
            print("That isnt even a number yah dingus!")
        elif int(user_input) < len(menu_choices):
            valid_input = True
    Converter.process(os.path.join(input_path,menu_choices[int(user_input)]),output_path,log_path)
    return user_menu(input_path,output_path,log_path)
