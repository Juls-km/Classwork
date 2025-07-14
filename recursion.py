# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     elif n > 2:
#         return fib(n-1) + fib(n-2)
# from gi.overrides.keysyms import value

# for number in range (500):
#   print(f"{number} : {fib(number)}")

f_cache = {}
value = 0

""" def fib_2(n) :
    if n in f_cache:
        return f_cache[n]
    if type(n)!=int:
        raise TypeError("n must be a positive int")
    elif n<1
        raise ValueError("n must be a positive int")

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib_2(n - 1) + fib_2(n - 2)

    f_cache[n] = value
    return value
#Memoization
for n in range (1,10):
    print(n,":", fib_2(n))
    print(f"{n} : {fib_2(n)}")"""

from functools import lru_cache


# least recently used  cache
@lru_cache(maxsize=100)
def fib3(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    elif k > 2:
        return fib3(k - 1) + fib3(k - 2)


for i in range(1, 100):
    print(f"{i} : {fib3(i)}")

for n in range(1, 51):
    print(fib3(n + 1) / fib3(n))


    # Sum of a list using recursion
    def list_sum(num_list):
        if len(num_list) == 1:
            return num_list[0]
        else:
            return num_list[0] + list_sum(num_list[1:])


    print(list_sum([2, 4, 5, 6, 7]))


    # Python of Sum of Nested lists using recursion
    def recursive_list_sum(data_list):
        total = 0
        for element in data_list:
         if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element
            return total
        print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))


# Sum of harmonic series
def harmonic_sum(l):
    if l < 2:  # base case for the harmonic sum
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)
    print(harmonic_sum(7))
    print(harmonic_sum(4))


# The tower of Hanoi
def TowerOfHanoi(m, source, destination_rod, auxiliary_rod):
    if m == 1:
        print("Move disk 1 from source", source, "to destination", destination_rod)
        return
    TowerOfHanoi(m - 1, source, auxiliary_rod, destination_rod)
    print("Move disk", m, "from source", source, "to destination", destination_rod)
    TowerOfHanoi(m - 1, auxiliary_rod, destination_rod, source)


m = 4
TowerOfHanoi(m, 'A', 'B', 'C')