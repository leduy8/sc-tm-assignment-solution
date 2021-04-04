from .exploding_kittens import main


# * Testcase 1
# * Sample input: cards = 56, players = 2
# * Sample output: 2.38%
# * 2.5%
# * 2.63%
# * 2.78%
# * 2.94%
# * 3.12%
# * 3.33%
# * 3.57%
# * 3.85%
# * 4.17%
# * 4.55%
# * 5.0%
# * 5.56%
# * 6.25%
# * 7.14%
# * 8.33%
# * 10.0%
# * 12.5%
# * 16.67%
# * 25.0%
# * 50.0%
def test_main_testcase_1(capfd):
    main(56, 2)
    out, err = capfd.readouterr()
    assert out == """2.38%
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
"""


# * Testcase 2
# * Sample input: cards = 56, players = 5
# * Sample output: 4.76%
# * 6.25%
# * 9.09%
# * 16.67%
# * 100.0%
def test_main_testcase_2(capfd):
    main(56, 5)
    out, err = capfd.readouterr()
    assert out == """4.76%
6.25%
9.09%
16.67%
100.0%
"""


# * Testcase 3
# * Sample input: cards = 56, players = 4
# * Sample output: 3.57%
# * 4.17%
# * 5.0%
# * 6.25%
# * 8.33%
# * 12.5%
# * 25.0%
def test_main_testcase_3(capfd):
    main(56, 4)
    out, err = capfd.readouterr()
    assert out == """3.57%
4.17%
5.0%
6.25%
8.33%
12.5%
25.0%
"""
