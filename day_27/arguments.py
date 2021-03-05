def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
print(add(1,2,3,4))
#args is a tuple
#kwargs is a dictionary
def calculate(**kwargs):
    pass