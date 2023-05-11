def berTripletCode(input, output):
    errorBits = 0 #counter of bits that differentiate between input and output
    for i in range(len(input)):
        errorBits = errorBits + (input[i] ^ output[i]) #XOR between input and output
    return errorBits/len(input)