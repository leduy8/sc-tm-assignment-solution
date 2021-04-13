
"""
Đề bài: Viết chương trình tìm các số nguyên tố trong một dãy số.
Problem: Write a program to find the prime numbers within a range of numbers.

Sample input: start = 3, end = 6
Sample output: 3
6

Sample input: start = 0, end = 4
Sample output: 3
"""


def main(start, end):
    for num in range(start, end + 1):
        if (num < 2):
            continue

        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            print(num)


main(2, 16)
