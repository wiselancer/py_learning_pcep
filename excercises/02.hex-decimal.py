hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    charset=tuple(hexNum)
    if len(hexNum) > 3 or not all(char in hexNumbers for char in charset):
        return None
    #base = int(max(hexNumbers))+1
    base = max(hexNumbers.values())+1
    result = 0
    multiplicator = 1
    for char in charset[::-1]:
        #print(f'number={hexNumbers[char]} * mult= {multiplicator} res={result}')
        result =hexNumbers[char] * multiplicator + result
        multiplicator *= base
    return result
