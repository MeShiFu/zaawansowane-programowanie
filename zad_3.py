def parzyste(number_list):
    for i in range(10):
        if number_list[i] % 2 == 0:
            print(number_list[i])


numbers = [3, 6, 8, 5, 2, 46, 1, 65, 75, 44]
parzyste(numbers)
