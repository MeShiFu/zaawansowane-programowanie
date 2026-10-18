def numbersx2(number_list):
    for number in number_list:
        newnumber = number * 2
        print(newnumber)
numbers = [3,6,8,5,2]
numbersx2(numbers)

def listnumberx2(number_list):
    newnumber = [number*2 for number in number_list]
    print(newnumber)
listnumberx2(numbers)
