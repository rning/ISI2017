def parameter(pname):
    parameters = open("./Parameters.txt")
    parameterVariables = list()
    varDict = dict()

    for line in parameters:
        parameterVariables = line.split(": ")
        tempVar = parameterVariables[0]
        tempVal = parameterVariables[1].strip("\n ")
        varDict[tempVar] = tempVal
    return varDict[pname]
# refer to variables with parameter({parameter}), which will return the parameter's value.

if __name__ == "__main__":
    print parameter(data)
