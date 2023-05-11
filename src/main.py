import CodeGenerator
import TripletCode
import HammingCode
import BCH_Code
import CodeDisruptor
import BitErrorRate

numOfBits = 16384
repetitions = 100

generator = CodeGenerator.RandomBitsGenerator(numOfBits)
bits = generator.generateBits()
tripletBits = TripletCode.encode(bits)
hammingBits = HammingCode.encode(bits)
bchBits = BCH_Code.encode(bits)

bsc = 0
ge = 0

for i in range(repetitions):
    disruptedBits = CodeDisruptor.disrupt(tripletBits, 0.1)
    gilbertTriplet = CodeDisruptor.GilbertEliot(tripletBits, 0.9, 0.1, 0.1)
    decodedBits = TripletCode.decode(disruptedBits)
    decodedBitsGilbert = TripletCode.decode(gilbertTriplet)
    
    bsc += BitErrorRate.berTripletCode(bits,decodedBits)
    ge += BitErrorRate.berTripletCode(bits,decodedBitsGilbert)

print(bsc/repetitions)
print(ge/repetitions)

bsc = 0
ge = 0

for i in range(repetitions):
    disruptedHamming = CodeDisruptor.disrupt(hammingBits, 0.1)
    gilberthamming = CodeDisruptor.GilbertEliot(hammingBits, 0.9, 0.1, 0.1)
    decodedHammin = HammingCode.decode(disruptedHamming)
    decodedHamminGilbert = HammingCode.decode(gilberthamming)
    
    bsc += BitErrorRate.berTripletCode(bits,decodedHammin)
    ge += BitErrorRate.berTripletCode(bits,decodedHamminGilbert)

print(bsc/repetitions)
print(ge/repetitions)

bsc = 0
ge = 0

for i in range(repetitions):
    disruptedbch = CodeDisruptor.disrupt(bchBits, 0.1)
    gilbertbch = CodeDisruptor.GilbertEliot(bchBits, 0.9, 0.1, 0.1)
    decodedbch = BCH_Code.decode(disruptedbch)
    decodedbchGilbert = BCH_Code.decode(gilbertbch)
    
    bsc += BitErrorRate.berTripletCode(bits,decodedbch)
    ge += BitErrorRate.berTripletCode(bits,decodedbchGilbert)

print(bsc/repetitions)
print(ge/repetitions)

bsc = 0
ge = 0
    #print(bits)
    #print(hammingBits)
    #print(disruptedHamming)
    #print(decodedHammin)
    #print(decodedHamming)

    #print(bits)
    #print(bchBits)
    #print(disruptedbch)
    #print(decodedbch)
    #print(decodedbchg)

    #print(bits)
    #print(disruptedBits)
    #print(decodedBits)
    #print(decodedBitsg)
    #print(BitErrorRate.berTripletCode(bits,decodedBits))




    #do uruchomienia przyda się starsza wersja NumPy: pip install numpy==1.23.5