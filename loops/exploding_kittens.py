
"""
Bài 3: Bạn và hội bạn của mình quyết định chơi bộ boardgame Mèo nổ (Exploding Kittens). Một bộ gồm 56 lá bài. Số người chơi từ 2-5 người. Số lá bài nổ bằng với số người chơi. Bắt đầu trò chơi, mỗi người được chia 7 lá bài. Tính và in ra màn hình tỉ lệ bạn bốc đúng lá bài nổ sau mỗi vòng bốc. 
(Giả sử mọi người chơi khác cũng không bốc trúng lá bài bom) 
(nếu kết quả là số thập phân thì lấy 2 số sau số sau dấu phẩy)

Exercise 3: You and your friends decided to play the Exploding Kittens board game. A deck contains 56 cards. Number of players from 2 to 5 people. The number of exploding cards is equal to the number of players. At the beginning of the game, each person is dealt 7 cards. Calculate and print on the screen the odds of you getting the exploding card after each draw. 
(Assuming every other player did not draw the exploding card either) 
(if the result is a decimal then take 2 numbers after the comma)

Sample input: cards = 56, players = 2
Sample output: 2.38%
2.5%
2.63%
2.78%
2.94%
3.12%
3.33%
3.57%
3.85%
4.17%
4.55%
5.0%
5.56%
6.25%
7.14%
8.33%
10.0%
12.5%
16.67%
25.0%
50.0%

Sample input: cards = 56, players = 5
Sample output: 4.76%
6.25%
9.09%
16.67%
100.0%
"""


def main(cards, players):
    # * Initial round
    cards = cards - (7 * players)
    while cards > 0:
        odds = (1 / cards) * 100
        print(f"{round(odds, 2)}%")

        cards = cards - players


main(56, 4)
