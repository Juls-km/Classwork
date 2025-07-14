for i in range(2, 30, 3):  #rang(start
       print(i, end=' ')

def check(num: float)-> float:
    if num <= 50.0:
        print("has passed")
    else:
        print("has not passed")
    return

def check_two(num: float)-> bool:
    if num<= 50:
        return True
    else:
        return False

def calc_area(radius: float)-> float:
    return 3.14 * (radius ** 2)


print(calc_area(7.2))

def sum_i(b: float, y:float)-> float:
    return b+y

def sum_ii(b: float, y:float)-> float:
    return b+y

def sum_iii(b: float, y:float)-> float:
    return b+y


check(89.9)
check_two(45.7)

has_passed: bool = check_two(30.2)
print(has_passed)