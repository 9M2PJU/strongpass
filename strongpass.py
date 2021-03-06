#!/usr/bin/env python3

# Program: strongpass.py
# Version: 3.3.0
# Description: Generate random passwords 
# 
# Copyright (C) 2015, 2016. 2017 Brainfuck 

# GNU GENERAL PUBLIC LICENSE
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse
import string
import secrets

# program name and version
_PROGRAM = "strongpass.py"
_VERSION = "3.3.0"


# banner
def banner():
    print("{} {}\n".format(_PROGRAM, _VERSION))
    print("Generate random passwords\n")


# print version and exit
def print_version():
    banner()
    print("License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>")
    print("This is free software: you are free to change and redistribute it.")
    print("There is NO WARRANTY, to the extent permitted by law.")
    exit(0)


# function for check the user input 
def check(input_args):
    input_args = int(input_args)
    if input_args > 254:
        raise argparse.ArgumentTypeError("please enter an integer no more bigger than 254")
        exit(1)
    else:
        return input_args


# main
def main():
    parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter)

    # type=check --> def check()
    parser.add_argument("-l", "--lenght", type=check, help="Lenght of password")
    parser.add_argument("-n", "--number", type=check, help="Number of password to generate")
    parser.add_argument("-v", "--version", action="store_true", help="display program version and exit")

    args = parser.parse_args()
    
    # if no arguments are given, print banner and help
    if len(sys.argv) == 1:
        banner()
        parser.print_help()
        exit(1)

    if args.version:
        print_version()
    
    """ generate password/s with 'secrets'
    charset are defined with variables
    characters excluded: l0Oo`ìèéòçà°
    """
    if args.lenght and args.number:
        for x in range(args.number):
            letters = "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"
            numbers = "123456789"
            special = "|\!$%&/()='?^~[]{}+*@#<>,;.:-_"               
            chars = letters + numbers + special
            password = "".join((secrets.choice(chars)) for x in range(args.lenght))
            print(password) 
    else:
        parser.error("the following arguments are required:: -l, --lenght <lenght> -n, --number <number>")
        exit(1)


if __name__ == "__main__":
    main()
