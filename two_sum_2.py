
def run(Input, target):
    for index, element in enumerate(Input):
        for i in reversed(range(index)):
            if element + Input[i] == target:
                return element, Input[i]

Input = [1, 3, 4, 5 , 6]
target = 9
Output = run(Input, target)
print(Output)
assert Output[0]+Output[1] == target, "False"
