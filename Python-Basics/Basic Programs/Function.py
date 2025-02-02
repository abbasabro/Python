from multiprocessing import reduction


def calc_sum(a,b):
    sum=a+b
    return sum
print(calc_sum(4,5))
print(calc_sum("hel","lo"))

def avg_three(a,b,c):
    avg=(a+b+c)/3
    return avg
print(avg_three(3,4,5))

def defualt_val(b,a=4):
    return a+b
print(defualt_val(5))