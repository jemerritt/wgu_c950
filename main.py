# Joseph Merritt

from packages import *
import distances


# User interface for WGUPS Routing System
# O(N^2)
class Main:
    print('\n        WGUPS Routing Information System\n        ________________________________')
    msg = """
        Please select from the following options or type 'quit' to quit:
        1. Get all package info at the entered time
        2. Get info for a single package at the entered time
        """

    user_input = input(msg)

    while True:
        if user_input.lower() == 'quit':
            print("Quiting...")
            break
        elif user_input == '1':
            prompt = """
            Please enter a time in the following 24-hour format or type 'quit' to quit:
            Example 09:17:00 or 13:45:00
            """
            user_input = input(prompt)
            if user_input.lower() == 'quit':
                print("Quiting...")
                break
            check_input = user_input.replace(":", "")
            try:
                check_input_int = int(check_input)
            except ValueError:
                print("Invalid Time")
                continue
            if len(check_input) < 6 or check_input_int < 0 or check_input_int > 240000:
                print("Invalid Time")
                continue
            all_packages = get_all_packages_at(check_input_int)
            for i in range(len(all_packages)):
                print("Package#:", all_packages[i][0], "| Address:", all_packages[i][1], "| City:", all_packages[i][2],
                      "| Zip:", all_packages[i][3], "| Weight:", all_packages[i][5], "| Deadline:", all_packages[i][4],
                      "| Status:", all_packages[i][8], all_packages[i][9])
        elif user_input == '2':
            prompt = """
            Please enter a time in the following 24-hour format or type 'quit' to quit:
            Example 09:17:00 or 13:45:00
            """
            user_input = input(prompt)
            if user_input.lower() == 'quit':
                print("Quiting...")
                break
            check_input = user_input.replace(":", "")
            try:
                check_input_int = int(check_input)
            except ValueError:
                print("Invalid Time")
                continue
            if len(check_input) < 6 or check_input_int < 0 or check_input_int > 240000:
                print("Invalid Time")
                continue
            user_input = input("Enter Package ID:")
            while int(user_input) < 1 or int(user_input) > 40:
                print("Invalid Package")
                user_input = input("Enter Package ID:")
            package = get_package_at(int(user_input), check_input_int)
            print("\nPackage#:", package[0][0], "| Address:", package[0][1], "| City:", package[0][2],
                  "| Zip:", package[0][3], "| Weight:", package[0][5], "| Deadline:", package[0][4],
                  "| Status:", package[0][8], package[0][9])
        else:
            user_input = input(msg)
