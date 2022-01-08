"""
import os

print(os.getcwd())

os.chdir(os.getcwd()+'/today')

os.system('mkdir today')
"""

import shutil

shutil.copyfile('standLib.py', 'standLib1.py')
