import os

def absPath():
    return os.path.dirname(os.path.abspath(__file__))

print(absPath())