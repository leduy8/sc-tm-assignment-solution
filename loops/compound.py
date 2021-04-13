
"""
Bài 2: Giả sử hiện tại bạn đang có 30.000$, bạn muốn đầu tư số tiền này vào một quỹ chỉ số với lãi suất hàng năm là 6%. Số tiền lãi của năm nay sẽ được cộng vào vốn cho năm sau.
a) Tính số tiền bạn sẽ nhận được sau 20 năm.
b) Mỗi tháng bạn bổ sung vào danh mục của mình 100$. Tính số tiền bạn sẽ nhận được sau 20 năm. (*)
(Nếu kết quả là số thập phân, lấy 2 số sau dấu phẩy)

Exercise 2: Assuming you currently have $30,000, you want to invest this money in an index fund with an annual interest rate of 6%. This year's interest will be added to the capital for the following year.
a) Calculate the amount you will receive after 20 years.
b) Each month you add $100 to your portfolio. Calculate the amount you will receive after 20 years. (*)
(If the result is a decimal then take 2 numbers after the comma)

Sample input: principle = 30000, year = 20, rate = 6
Sample output: 96214.06
"""


def main(principle, year, rate):
    amount = 0
    for i in range(1, year + 1):
        amount = principle * (pow((1 + rate / 100), i))
        # print(f"After {i} years, Amount = {round(amount, 2)}")
    print(round(amount, 2))


main(10000, 5, 6)
