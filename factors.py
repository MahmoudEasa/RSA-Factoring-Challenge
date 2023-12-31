#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line == '\n':
            break
        num = int(line)
        found = 0

        for i in range(2, (num//2) + 1):
            if num % i != 0:
                continue

            front = 2
            last = (num//2) + 1

            for j in range(front, last):
                mod = (front + last) // 2
                if num % mod != 0:
                    if i * mod <= num:
                        front = mod + 1
                    else:
                        last = mod - 1
                    continue

                if i * mod == num:
                    print(f"{num}={mod}*{i}")
                    found = 1
                    break
                elif i * mod < num:
                    front = mod + 1
                else:
                    last = mod - 1

            if found:
                break
