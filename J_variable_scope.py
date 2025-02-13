result = 3


def scope_test1():  # scope is how visible a variable is. parameters and variables inside a function, have a scope of that function (only see what is available to that function) have
    #  this variable shadows (hides) result from outer scope
    result = 42
    print("Result inside the function:", result)


scope_test1()
print("Result outside the function:", result)

# ############################################


def scope_test2():
    # instruction to use the global variable inside this function
    global result # change global result of 3 and change it
    result = 42 #don't use global. give your functions their own parameters
    print("Result inside the function:", result)


print("=" * 30)
scope_test2()
print("Result outside the function:", result) # does not see what is in line 16-20
