parameters = open("./Parameters.txt")
parameterVariables = list()
varDict = dict()

for line in parameters:
    parameterVariables = line.split(": ")
    tempVar = parameterVariables[0]
    tempVal = parameterVariables[1].replace("\n", "")
    varDict[tempVar] = tempVal

# print varDict - debug to see if variable dictionary is working

# refer to variables with varDict["variableName"]
