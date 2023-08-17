
def run(Input, target):
    for i in range(len(Input)):
        for j in range(i+1,len(Input)):
            if (target == Input[i] + Input[j]):
                return Input[i],Input[j]

Input = [1,7,2]
target = 9
Output = run(Input, target)
print(Output)
assert Output[0]+Output[1] == target," Sum of two numbers not correct"








