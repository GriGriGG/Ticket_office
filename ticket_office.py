qnt = int(input("Enter quantity of tickets:\n"))
total_cost = 0
num_adults = 0

for _ in range(qnt):
    age = int(input("Enter visitor age:\n"))

    if age < 18:
        continue
    elif age >= 18 and age < 25:
        total_cost += 990
        num_adults += 1
    else:
        total_cost += 1390
        num_adults += 1

if num_adults == 0:
    print("Come on, kids!")
else:
    print("The cost of your tickets:", total_cost, "rub.")

    if qnt > 3 and num_adults > 0:
        discount = total_cost * 0.1
        total_cost -= discount
        discount_amount = total_cost * 0.1
        print("Discount is:", "%.2f" % discount_amount, "rub.")
        print("To pay:", "%.2f" % total_cost, "rub.")
    else:
        print("To pay:", "%.2f" % total_cost, "rub.")

