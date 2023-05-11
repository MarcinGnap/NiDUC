import komm

#tutaj parametry (długość_segmentu, liczba_korekcji_błędów)
bch = komm.BCHCode(3, 1)

def encode(input):
    if len(input) % 4 != 0:
        raise ValueError()
    
    #kodowanie odbywa się na 7 bitach
    output = []
    for i in range(0, len(input), 4):
        output.extend(bch.encode(input[i:i+4]))

    return output

def decode(input):
    if len(input) % 7 != 0:
        raise ValueError()

    output = []
    for i in range(0, len(input), 7):
        output.extend(bch.decode(input[i:i+7]))

    return output
