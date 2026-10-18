def czyZawiera(num_list: list, num: int)->bool:
    return num in num_list
print(czyZawiera([1, 2, 3, 4, 5], 3))
print(czyZawiera([1, 2, 3, 4, 5], 8))