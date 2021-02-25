#!/usr/bin/env python3

# test application.py

# Imports
from application import *


# Functions
def test_get_os():
    assert get_operating_system() == "Windows"


def main():
    result = get_operating_system()
    print(result)


if __name__ == "__main__":
    main()
