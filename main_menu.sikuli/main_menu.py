from sikuli import *
import sys
import os
import time


main_menu = ("Standard", "Date")
selected = select("Please select an item from the list", options = main_menu)

if selected == items[0]:
   popup("You did not select an item")
   exit(1)
