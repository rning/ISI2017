parameters = open("./Parameters.txt")
parameterVariables = list()
varDict = dict()

for line in parameters:
    parameterVariables = line.split(": ")
    tempVar = parameterVariables[0]
    tempVal = parameterVariables[1].replace("\n", "")
    varDict[tempVar] = tempVal
    
# refer to variables with varDict["variableName"]