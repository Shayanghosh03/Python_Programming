'''
def cal_prod(a,b):
    return a*b
cal_prod() #Error

'''
def cal_prod(a=2,b=3):
    print(a*b)
    return a*b
cal_prod()

def cal_prod(a,b=2):
    print(a*b)
    return a*b
cal_prod(6)

'''
def cal_prod(a=2,b):
    print(a*b)
    return a*b
cal_prod(6) #Error

'''
