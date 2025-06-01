def bin_issquare(num):
    left, right = 1, num
    while left <= right:
        mid = (left+right)//2
        
        if mid*mid == num:
            return True
        elif mid*mid > num:
            right = mid-1 #Обязательно смещать на 1! Если не смещать, то может настать такой момент, когда left и right просто не будут меняться и уикл будет бесконечным
        else:
            left = mid+1 #Обязательно смещать на 1!
    return False

print(bin_issquare(185)) 