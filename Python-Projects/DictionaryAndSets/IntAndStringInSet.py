#Can we have int(18) and '18' string in a set let's check

thisset={18,'18'}
print(thisset)

s1={}
print(type(s1)) #Dictionary

s=set(())
s.add(20)
s.add('20')
print(len(s))
