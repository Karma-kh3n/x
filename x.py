import os, sys
os.system('clear')
try:
    __import__("x").mst()
except Exception as e:
    exit(str(e))
