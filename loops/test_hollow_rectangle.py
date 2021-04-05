from .hollow_rectangle import main


# * Testcase 1
# * Sample input: rows = 3, cols = 4
# * Sample output: ****
# * *  *
# * ****
def test_main_testcase_1(capfd):
    main(3, 4)
    out, err = capfd.readouterr()
    assert out == """****
*  *
****
"""


# * Testcase 2
# * Sample input: rows = 6, cols = 2
# * Sample output: **
# * **
# * **
# * **
# * **
# * **
def test_main_testcase_2(capfd):
    main(6, 2)
    out, err = capfd.readouterr()
    assert out == """**
**
**
**
**
**
"""


# * Testcase 3
# * Sample input: rows = 1, cols = 1
# * Sample output: *
def test_main_testcase_3(capfd):
    main(1, 1)
    out, err = capfd.readouterr()
    assert out == """*
"""


# * Testcase 4
# * Sample input: rows = -3, cols = 2
# * Sample output: ""
def test_main_testcase_4(capfd):
    main(-3, 2)
    out, err = capfd.readouterr()
    assert out == ""


# * Testcase 5
# * Sample input: rows = 3, cols = -2
# * Sample output: ""
def test_main_testcase_5(capfd):
    main(3, -2)
    out, err = capfd.readouterr()
    assert out == ""


# * Testcase 6
# * Sample input: rows = 3.5, cols = 4
# * Sample output: ""
def test_main_testcase_6(capfd):
    main(3.5, 4)
    out, err = capfd.readouterr()
    assert out == ""
