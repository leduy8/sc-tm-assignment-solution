
"""
Bài 2: Cho một xe chở hàng với X đơn vị diện tích. Tạo một mảng với các dictionary bên trong bao gồm 2 key: Số lượng hàng và đơn vị diện tích của mỗi hàng. In ra kết quả xem với số lượng hàng cho trước có đủ chỗ để xe chở hàng chở trong một lượt không?
Exercise 2: Given a truck with X units of area. Create an array with dictionaries inside including 2 keys: Number of rows and area unit of each row. Print out the results to see if the number of goods is enough for the cargo truck to carry in one turn?

Sample input: cargos = [
                          {"number_of_cargos": 5, "unit_per_cargo": 2},
                          {"number_of_cargos": 3, "unit_per_cargo": 3},
                          {"number_of_cargos": 1, "unit_per_cargo": 1}
                       ], truck_size=10
Sample output: "There's too many cargo for the truck to deliver in 1 go."

Sample input: cargos = [
                          {"number_of_cargo": 3, "unit_per_cargo": 2},
                          {"number_of_cargo": 1, "unit_per_cargo": 3},
                          {"number_of_cargo": 1, "unit_per_cargo": 1}
                       ], truck_size=20
Sample output: "There is enough cargo for the truck to deliver in 1 go."
"""


def main(cargos, truck_size):
    total_cargo_space = 0

    for cargo in cargos:
        total_cargo_space += cargo["number_of_cargos"] * \
            cargo["unit_per_cargo"]

    if (total_cargo_space > truck_size):
        print("There's too many cargo for the truck to deliver in 1 go.")
    else:
        print("There is enough cargo for the truck to deliver in 1 go.")


main(cargos=[
    {"number_of_cargos": 3, "unit_per_cargo": 2},
    {"number_of_cargos": 1, "unit_per_cargo": 3},
    {"number_of_cargos": 1, "unit_per_cargo": 1}
], truck_size=20)
