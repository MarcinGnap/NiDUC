def encode(input):
    #znalezienie długości danych/obliczenie ilości bitów parzystości
    pBitsCount = 0
    while 2 ** pBitsCount < len(input) + pBitsCount + 1:
        pBitsCount += 1

    output = [0] * (len(input) + pBitsCount)
    j = 0
    for i in range(len(output)):
        if i+1 == 2 ** j:
            #omienięcie pozycji bitów parzystości
            j += 1
        else:
            output[i] = input[i-j]

    #kodowanie bitów parzystości
    for i in range(pBitsCount):
        pos = 2 ** i - 1
        sum = 0
        j = pos
        while j < len(output):
            for k in range(pos+1):
                if j < len(output):
                    #XOR
                    sum ^= output[j]
                    j += 1
            j += pos + 1
        output[pos] = sum

    return output

def decode(input):
    error_bit = 0
    pBitsCount = getNumParity(input)
    pBits = [0] * pBitsCount
    #odczytywanie wartości bitów parzystości
    for i in range(pBitsCount):
        pBits[i] = input[(2**i)-1]
    #obliczenie wartości błędnego bitu
    for i in range(pBitsCount):
        if checkParity(input, 2**i):
            error_bit += 2**i
    #jeśli wykryto błąd to naprawimay go
    if error_bit > 0 and error_bit <= len(input):
        input[error_bit-1] ^= 1
    #usuwanie bitów parzystości
    output = [input[i] for i in range(len(input)) if i+1 not in [2**j for j in range(pBitsCount)]]

    return output

def getNumParity(input):
    for i in range(len(input)):
        if 2**i >= len(input) + i + 1:
            return i

def checkParity(input, bit):
    # Tworzymy maskę bitową na podstawie wartości bit.
    mask = [((i+1) & bit) != 0 for i in range(len(input))]
    # Zwracamy True, jeśli liczba jedynek jest nieparzysta.
    return sum([input[i] for i in range(len(input)) if mask[i]]) % 2 != 0