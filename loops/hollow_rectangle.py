
"""
Bài 4: Viết chương trình vẽ hình chữ nhật rỗng bằng dấu sao ( “*” )
(Số hàng và số cột phải là số dương lớn hơn 0)
Exercise 4: Write a program to print hollow rectangle star pattern.
(Number of rows and columns must be a positive number greater than 0)

Sample input: row = 3, column = 4
Sample output: ****
*  *
****
"""


def main(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if(i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()


main(3, 4)
