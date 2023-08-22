

def run():
    frh = open("machine-readable-business-employment-data-mar-2023-quarter.csv", "r")
    fwh = open("swapedfile.csv", "w")
    for x in frh:
        x = x.split(",")
        x[2],x[7] = x[7],x[2]
        fwh.write(",".join(x))

    frh.close()
    return fwh


outputfile = run()
outputfile.close()





