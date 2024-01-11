# 23.8.2023

# Project Euler 16
# Power Digit Sum

# What is the sum of the digits of 2^1000?

# Feel like I'm missing something here .... ? (it does work, though)

n = 2**1000

s = 0

for a in str(n):
    s += int(a)

print (s)