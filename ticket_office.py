kids = 0
young = 990
adults = 1390

tickets = 0
qnt = int(input("Enter quantity of tickets:\n"))
for age in range(qnt):
    age = int(input("Enter visitor age:\n"))
    if age < 18:
        tickets = qnt + kids
    elif age >= 18 and age <= 25:
        tickets = qnt + young
    elif age > 25:
        tickets = qnt + adults
if tickets == 0:
    print("Come on, kids!")

else:
    print("The cost of your tickets:", "%.2f" % tickets)

if qnt > 3:
    discount = tickets / 100 * 10
    print("Discount is:", "%.2f" % discount)
    print("To pay:", "%.2f" % (tickets-discount))
