# lambda functions are anonymous short-hand functions
# lambda is a short in-situ piece of logic that you can use instead of a function
# if using a lambda in more than one place, use a function instead
print("######## Example 1 ########")
compare = lambda a, b: -1 if a < b else (+1 if a > b else 0) # return -1 if parameter of b is < a
# else (+1 if a > b else 0) means if a > b, return +1  else 0. sorted  logics return +1 if they return early, otherwise -1
x = 42
y = 3

# print("a > b returns:", compare(x, y))
print(f"{x} > {y} returns:", compare(x, y))

x = 2
print(f"{x} > {y} returns:", compare(x, y))

x = 3
print(f"{x} > {y} returns:", compare(x, y))

print("######## Example 2 ########")
numbers_list = [0, 1, 2, 3, 5, 8, 13, 21]
print(f"Original list of numbers: {numbers_list}")

numbers_plus1_list = list(map(lambda num: num + 1, numbers_list))
print(f"New list of numbers plus 1: {numbers_plus1_list}")

numbers_times10_list = list(map(lambda num: num * 10, numbers_list))
print(f"New list of numbers x 10: {numbers_times10_list}")

numbers_squared_list = list(map(lambda num: num * num, numbers_list))
print(f"New list of numbers squared: {numbers_squared_list}")
