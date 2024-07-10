def cal(num):
    if(num==0):
        return 0
    return cal(num-1)+num
print(cal(5))