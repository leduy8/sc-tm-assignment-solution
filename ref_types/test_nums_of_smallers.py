from .nums_of_smallers import main


# * Testcase 1
# * Input: arr = [5, 2, 3, 5]
# * Output: [2, 0, 1, 2]
def test_main_testcase_1(capfd):
    main([5, 2, 3, 5])
    out, err = capfd.readouterr()
    assert out == """[2, 0, 1, 2]
"""


# * Testcase 2
# * Input: arr = [1, 1, 1, 1]
# * Output: [0, 0, 0, 0]
def test_main_testcase_2(capfd):
    main([1, 1, 1, 1])
    out, err = capfd.readouterr()
    assert out == """[0, 0, 0, 0]
"""


# * Testcase 3
# * Input: arr = [-5, 1, 6, -9]
# * Output: [1, 2, 3, 0]
def test_main_testcase_3(capfd):
    main([-5, 1, 6, -9])
    out, err = capfd.readouterr()
    assert out == """[1, 2, 3, 0]
"""
