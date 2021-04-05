from .primes import main


# * Testcase 1
# * Input: start = 3, end = 6
# * Output: 3
# * 5
def test_main_testcase_1(capfd):
    main(3, 6)
    out, err = capfd.readouterr()
    assert out == """3
5
"""


# * Testcase 2
# * Input: start = 10, end = 40
# * Output: 11
# * 13
# * 17
# * 19
# * 29
# * 31
# * 37
def test_main_testcase_2(capfd):
    main(10, 40)
    out, err = capfd.readouterr()
    assert out == """11
13
17
19
23
29
31
37
"""


# * Testcase 3
# * Input: start = 0, end = 2
# * Output: ""
def test_main_testcase_3(capfd):
    main(0, 2)
    out, err = capfd.readouterr()
    assert out == """2
"""


# * Testcase 4
# * Input: start = -3, end = 0
# * Output: ""
def test_main_testcase_4(capfd):
    main(-3, 0)
    out, err = capfd.readouterr()
    assert out == ""


# * Testcase 5
# * Input: start = 2, end = 16
# * Output: 3
# * 5
def test_main_testcase_5(capfd):
    main(2, 16)
    out, err = capfd.readouterr()
    assert out == """2
3
5
7
11
13
"""
