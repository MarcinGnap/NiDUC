import random

def disrupt(input: list, probability:float) ->list:
    output = []

    for i in range(0, len(input)):
        randomNumber = random.randint(1,100)
        if randomNumber < probability*100:
            if input[i] == 0:
                output.append(1)
            else :
                output.append(0)
        else:
            output.append(input[i])
    return output

def GilbertEliot(input: list, p_good: float,p_bad: float, error_rate: float):
    output = []
    is_bad = False

    for i in input:
        if is_bad:
            if random.random() < error_rate:
                output.append((i + 1) % 2)
            else:
                output.append(i)
            is_bad = random.random() < p_good
            continue
        output.append(i)
        is_bad = random.random() < p_bad

    return output