

def length_checker(name):
    other_names = []
    for n in name:
        if len(n) >= 5:
            other_names.append(n)

    return other_names        

names = ['Ali','Abbas','Hussain','Farhan','Faris']

others = length_checker(names)

print(others)