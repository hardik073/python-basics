

#Packages are just Python files containing code - typically combinations of functions and classes.
#Built-in: Come with Python installation
#External: Downloaded from the internet into your virtual enviornment

# Web Scrapping: Extract data from websites
# Data Analysis: Process speadsheets and databases
# AI/ML: Build intelligent applications
# APIs: Connect to online services
# Automation: Control your computer

"""
Module: A single Python file (like math.py)
Package: A folder containing multiple modules
Function: A reusable block of code (like print() or sqrt())
Class: A blueprint for creating objects (we’ll cover this later)

Think of it like this:

A module is like a toolbox
A package is like a garage with multiple toolboxes
A function is like a specific tool (hammer, screwdriver)
A class is like a blueprint for building tools
"""


# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)


#Common Built-in modules

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)


# ------------ Different methods of import -------------#

# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
circle_area = pi * radius ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *


# --------- Installing package --------------------- #

# Install a package
#pip install requests

# Install specific version
#pip install requests==2.28.0

# Install multiple packages
#pip install pandas numpy matplotlib



# --------- Finding package --------------------- #
"""
Finding packages

Where to find packages:

PyPI - Official Python package index
Awesome Python - Curated list
ChatGPT - Ask “What Python package should I use for [task]?” - Great for recommendations and comparisons
Google “Python package for [task]”

"""
