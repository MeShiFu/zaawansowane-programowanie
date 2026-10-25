def czyParzysta(num: int) -> bool:
    return num % 2 == 0


num1 = czyParzysta(1)
num2 = czyParzysta(2)

if num1:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

if num2:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
