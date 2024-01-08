#!/usr/bin/env python3

# def print_fibonacci(length):
#     sum;
#     if len(length) > 2:
#         sum = length[-1] + length[-2]

#     return sum

def print_fibonacci(length):
    if length <= 0:
        print("Length should be a positive integer.")
        return
    
    sequence = [0, 1]
    
    for _ in range(2, length):
        number = sequence[-1] + sequence[-2]
        sequence.append(number)
    
    print(sequence)