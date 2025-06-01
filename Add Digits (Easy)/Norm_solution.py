def addDigits(num: int) -> int:
    while num > 9:
        num = sum(map(int,str(num)))
    return num

print(addDigits(76))

def addDigits2(num: int) -> int:
    while num > 9:
        num = num//10 + num%10
    return num

print(addDigits2(76))

def addDigits3(num: int) -> int: #Самое быстрое решение
    while num > 9:
        sum = 0
        while num:
            sum += num%10
            num = num//10
        num = sum
    return num

print(addDigits3(76))