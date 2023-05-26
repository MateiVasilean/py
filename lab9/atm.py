avalaible_bills = []
bills = ['0', '1', '2', '5', '10', '20', '50', '100']

with open("/Users/matei/Documents/lab9/limits.txt") as f:
    for line in f:
        bill, count = map(int, line.strip().split())
        if bill in bills:
            avalaible_bills.append((bill, count))

available_money = 0
for bill, count in avalaible_bills:
    available_money += int(bill) * int(count)

USER_VALUE = int(input("Insert how many dollars you want to extract: "))
MAX_BILLS_INDEX = int(input("Insert the value of the biggest bill you want to receive:\n1. 1$ bill\n2. 2$ bill\n3. 5$ bill\n4. 10$ bill\n5. 20$ bill\n6. 50$ bill\n7. 100$ bill\n"))

if available_money >= USER_VALUE:
    withdraw_bills = []
    for i in range(MAX_BILLS_INDEX):
        num_bills = min(int(USER_VALUE / int(bills[MAX_BILLS_INDEX - i])), available_money[i])
        withdraw_bills.append(num_bills)
        USER_VALUE -= num_bills * int(bills[MAX_BILLS_INDEX - i])
        if USER_VALUE == 0:
            break
    if USER_VALUE == 0:
        print("You get:")
        for i in range(MAX_BILLS_INDEX):
            if withdraw_bills[i] > 0:
                print("{} bill(s) of {}$".format(withdraw_bills[i], int(bills[MAX_BILLS_INDEX - i])))
    else:
        print("Sorry, the ATM doesn't have enough bills")