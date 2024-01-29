"""
File name   : createFilesofDrivers.py
Author      : Mohamed Hussein
created on  : 29 / 1 /24
Description : A script of python to create  the essential files of drivers for each driver in embedded system
"""

def create_file(file_name, content=""):
    with open(file_name, "w") as file:
        file.write(content)


def generate_driver_files(driver_name):

    program_c_content = f"""\
#include "{driver_name}_interface.h"
#include "{driver_name}_private.h"

// Implementation of {driver_name} driver functions
// Add your code here
"""


    cfg_c_content = f"""\
#include "{driver_name}_cfg.h"
// Configuration parameters for {driver_name} driver
// Add your configuration code here
"""

    cfg_h_content = f"""\
#ifndef {driver_name.upper()}_CFG_H
#define {driver_name.upper()}_CFG_H

// Configuration parameters for {driver_name} driver
// Add your configuration code here

#endif /* {driver_name.upper()}_CFG_H */
"""

    interface_h_content = f"""\
#ifndef {driver_name.upper()}_INTERFACE_H
#define {driver_name.upper()}_INTERFACE_H

// Interface functions for {driver_name} driver
// Add your interface function declarations here

#endif /* {driver_name.upper()}_INTERFACE_H */
"""

    private_h_content = f"""\
#ifndef {driver_name.upper()}_PRIVATE_H
#define {driver_name.upper()}_PRIVATE_H

// Private definitions for {driver_name} driver
// Add your private definitions here

#endif /* {driver_name.upper()}_PRIVATE_H */
"""

    # Create files
    create_file(f"{driver_name}_program.c", program_c_content)
    create_file(f"{driver_name}_cfg.c", cfg_c_content)
    create_file(f"{driver_name}_cfg.h", cfg_h_content)
    create_file(f"{driver_name}_interface.h", interface_h_content)
    create_file(f"{driver_name}_private.h", private_h_content)


if __name__ == "__main__":

    while True :
        driver_name = input("Enter the name of the driver: ")
        generate_driver_files(driver_name)
        print(f"Files for {driver_name} driver created successfully.")

