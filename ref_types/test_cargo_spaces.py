from .cargo_spaces import main


# * Testcase 1
# * Input: cargos = [
# *                     {"number_of_cargos": 5, "unit_per_cargo": 2},
# *                     {"number_of_cargos": 3, "unit_per_cargo": 3},
# *                     {"number_of_cargos": 1, "unit_per_cargo": 1}
# *                 ], truck_size=10
# * Output: "There's too many cargo for the truck to deliver in 1 go."
def test_main_testcase_1(capfd):
    main(cargos=[
        {"number_of_cargos": 5, "unit_per_cargo": 2},
        {"number_of_cargos": 3, "unit_per_cargo": 3},
        {"number_of_cargos": 1, "unit_per_cargo": 1}
    ], truck_size=10)
    out, err = capfd.readouterr()
    assert out == """There's too many cargo for the truck to deliver in 1 go.
"""


# * Testcase 2
# * Input: cargos = [
# *                     {"number_of_cargos": 3, "unit_per_cargo": 2},
# *                     {"number_of_cargos": 1, "unit_per_cargo": 3},
# *                     {"number_of_cargos": 1, "unit_per_cargo": 1}
# *                 ], truck_size=20
# * Output: "There's too many cargo for the truck to deliver in 1 go."
def test_main_testcase_2(capfd):
    main(cargos=[
        {"number_of_cargos": 3, "unit_per_cargo": 2},
        {"number_of_cargos": 1, "unit_per_cargo": 3},
        {"number_of_cargos": 1, "unit_per_cargo": 1}
    ], truck_size=20)
    out, err = capfd.readouterr()
    assert out == """There is enough cargo for the truck to deliver in 1 go.
"""


# * Testcase 3
# * Input: cargos = [
# *                     {"number_of_cargos": 3, "unit_per_cargo": 2},
# *                     {"number_of_cargos": 1, "unit_per_cargo": 3},
# *                     {"number_of_cargos": 1, "unit_per_cargo": 1}
# *                     {"number_of_cargos": 2, "unit_per_cargo": 5}
# *                 ], truck_size=20
# * Output: "There's too many cargo for the truck to deliver in 1 go."
def test_main_testcase_3(capfd):
    main(cargos=[
        {"number_of_cargos": 3, "unit_per_cargo": 2},
        {"number_of_cargos": 1, "unit_per_cargo": 3},
        {"number_of_cargos": 1, "unit_per_cargo": 1},
        {"number_of_cargos": 2, "unit_per_cargo": 5}
    ], truck_size=20)
    out, err = capfd.readouterr()
    assert out == """There is enough cargo for the truck to deliver in 1 go.
"""
