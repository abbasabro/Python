monthly_expenses = [2200,2350,2600,2130,2190]

#In Feb, how many dollars you spent extra compare to January?
print( f"Extra expenses : {monthly_expenses[1]-monthly_expenses[0]}")
#Find out your total expense in first quarter (first three months) of the year.
total_expenses = 0
for n in range(3):
    total_expenses += monthly_expenses[n]
print(f"Quarter Total Expenses : {total_expenses}")

# Find out if you spent exactly 2000 dollars in any month   
print(f"Exact 2000 spent in any month {2000 in monthly_expenses}")

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenses.append(1980)   #june expenses added

'''You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''
monthly_expenses[3]-=200




