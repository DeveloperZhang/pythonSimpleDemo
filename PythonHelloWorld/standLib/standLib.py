"""
import os

print(os.getcwd())

os.chdir(os.getcwd()+'/today')

os.system('mkdir today')
"""
import datetime

"""
import shutil

shutil.copyfile('standLib.py', 'standLib1.py')

"""

"""
import glob

print(glob.glob('*.py'))

# ['standLib.py', 'standLib1.py']

"""
"""
import math

print(math.cos(math.pi / 4))

# 0.7071067811865476
"""

"""
import random

print(random.choice(['apple', 'pear']))

# apple

print(random.sample(range(100), 10))

# [20, 68, 23, 56, 63, 90, 34, 54, 2, 64]

print(random.random())

# 0.303429125049565

print(random.randrange(6))

# 4
"""

"""
from urllib.request import urlopen

for line in urlopen('http://127.0.0.1:8080/a.html'):
    line = line.decode('utf-8')
    print(line)

# Hello World!

"""

"""
from datetime import date

now = date.today()
print(now)
myDate = datetime.date(2022, 1, 2)
print(myDate.strftime("%y-%m-%d. %d %b %Y is a %A on %d day of %B. "))

distance = now - myDate
print(distance.days)

"""

