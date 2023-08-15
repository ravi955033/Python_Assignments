

num1 = [9,9]
num2 = [0,9,9]
result = []

def add_two_numbers(num1, num2):
    carry = 0
    for i in range(max(len(num1),len(num2))): # -> 4,3,2,1,0
        index1= (len(num1)-1) - i
        index2 = (len(num2)-1) - i
        if index1 >= 0:
            digit1 = num1[index1] + carry
        else:
            digit1 = 0 + carry

        if index2 >= 0:
            digit2 = num2[index2]
        else:
            digit2 = 0

        sum = digit1 + digit2
        digit = sum % 10
        result.insert(-i,digit)
        carry = sum // 10

    if (carry > 0):
        result.insert(0, carry)
    print(result)

    return result

assert add_two_numbers(num1, num2) == [1,9,8]," Sum of two numbers not correct"








