#!/usr/bin/python3

# create new child processes
import subprocess

# size of allocated memory
size = 10000000


print("Before memory allocation")
subprocess.run("free")


# memory allocation
array = [0]*size

print("After memory allocation")
subprocess.run("free")
