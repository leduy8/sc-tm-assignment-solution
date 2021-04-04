from .compound import main


# * Testcase 1
# * Input: principle = 30000, year = 20, rate = 6
# * Output: 96214.06
def test_main_testcase_1(capfd):
    main(30000, 20, 6)
    out, err = capfd.readouterr()
    assert out == "96214.06\n"


# * Testcase 2
# * Input: principle = 36000, year = 10, rate = 8
# * Output:
def test_main_testcase_2(capfd):
    main(36000, 10, 8)
    out, err = capfd.readouterr()
    assert out == "77721.3\n"


# * Testcase 3
# * Input: principle = 10000, year = 5, rate = 6
# * Output:
def test_main_testcase_3(capfd):
    main(10000, 5, 6)
    out, err = capfd.readouterr()
    assert out == "13382.26\n"
