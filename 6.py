meal = float(input('insert cost: '))

tax = meal*0.22

tip = meal*0.18

print(f'Tax is:  {format(tax, ".2f")} $ \n Tip is: {format(tip, ".2f")} $ \n The total is: {format(meal+tax+tip, ".2f")} $  ')
