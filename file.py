def readFileString(filename):
    return readFileLines(filename)[0]
    
def readFileLines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()
