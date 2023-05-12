# First we define the function
def sayhi(name, age):
    print("Hello " + name + ", You are " + str(age) + " years old")
    print("Hey there " + name + ", Heard you are turning " + str(age) + " years")

    # In order to display / execute function we have to call the function first


sayhi("Mike", 20)
sayhi("Tom", 25)


# RETURN STATEMENT
def cube(num):
    return num * num * num


result = cube(4)
print(str(result))


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 40, 5))
