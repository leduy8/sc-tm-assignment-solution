
"""
Đề bài: Cho một mảng gồm các số nguyên. In ra kết quả là mảng với số lượng số trong mảng nhỏ hơn số tại vị trí đó (không bao gồm chính số đó).
Problem: Given an array of integers. Print the result as an array with the number of numbers in the array less than the number at that position (excluding the number itself).

Sample input: [5, 2, 3, 5]
Sample output: [2, 0, 1, 2]
"""


def main(arr):
    res = []
    count = 0

    # * Check how many numbers in the array is smaller than the number in the index
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i] > arr[j]):
                count += 1
        res.append(count)
        count = 0

    print(res)


main([5, 2, 3, 5])
