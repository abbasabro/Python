

temp_value = input("Enter the Temperature with Unit (C/F/K) with a space : ").upper()
value_unit_list = temp_value.split(' ')
value = float(value_unit_list[0])

if 'C' in value_unit_list:
    kelvin = value + 273.15
    faren = value*(9/5) + 32
    print(f"{value}C converted into {round(kelvin,3)}K and {round(faren,3)}F")
elif 'F' in value_unit_list:
    celsuius = (value-32)*(5/9)
    kelvin = celsuius + 273.15
    print(f"{value}F converted into {round(kelvin,3)}K and {round(celsuius,3)}C")
elif 'K' in value_unit_list:
    celsuius = value - 273.15
    faren = celsuius*(9/5) + 32
    print(f"{value}K converted into {round(celsuius,3)}C and {round(faren,3)}F")
else:
    print("Invalid Unit")


