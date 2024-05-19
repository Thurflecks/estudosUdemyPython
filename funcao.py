def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def pi(x):
    if x % 2 == 0:
        return "par"
    return "impar"
    
vasco = multi(5,1)
parOuImpar = pi(vasco)
print(vasco, parOuImpar)

        