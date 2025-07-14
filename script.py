# str-string
# int
# float
# bool
# bytes
# tuple

# list
# set
# dict
name: str = "John doe"
age: int = 20
aggregate: float = 77.9
is_raining: bool = False

x: tuple = (1, 2, 3)
list_name: list = ["John", "Mary"]
num: list = [156, 5, 6, 9, 322, 29, 29]
print(num)
print(list_name)
data: dict = {'name': 'Bob', 'age': 20}

# functions
def get_largest(numbers, n):
    numbers.sort()
    return numbers[-n:]

# sorted_list = get_largest(nums, n:5)
# print(sorted list)

for x in range(10):
    print(x)

fruits = ['apple', 'cherry', 'kiwi']
for i in fruits:
    print(i)

for i in range(2, 30):
    print(i)