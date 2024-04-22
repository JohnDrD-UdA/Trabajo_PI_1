def is_Prime(n:int)->bool:
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sum_Prime(n:int)->int:
    sum:int=0

    for i in range(2,n+1):
        if is_Prime(i):
            sum+=i
    return sum

print(sum_Prime(5))
