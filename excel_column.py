
letterlist = []

def run(num):
    i = 0
    firstdigit = 0
    if num > 26 and num <= 16384:
        digit0 = num % 26
        if digit0 == 0:
            digit0 = 26
            num2 = num - 26
        else:
            num2 = num - digit0

        while (num2 >= 1):
            nof26s = num2//26
            remnof26s = nof26s % 26
            digit1 = nof26s - remnof26s
            if remnof26s != 0:
                letterlist.insert(i ,remnof26s)
                num2 = (digit1 * 26)
            else:
                firstdigit +=1
                if firstdigit == 1:
                    letterlist.insert(0, firstdigit)
                else:
                    letterlist[0] = firstdigit
                num2 = (digit1 * 26) - 26 * 26
            i += 1
        letterlist.insert(i, digit0)
    elif num > 0 and num < 26:
        letterlist.insert(i ,num )

    column = ""
    for j in letterlist:
        column += str(chr(j + 64))

    return column

Output = run(16384)
print(Output)
assert Output == "XFD"

