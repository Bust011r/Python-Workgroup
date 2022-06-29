liter_or_less = int(input('Quantity of container one liter or less: '))
more_then_liter = int(input('Quantity of container more then liter: '))


price = (liter_or_less * 0.10) + (more_then_liter * 0.25)

print(f'The price is {format(price, ".2f")} $')
