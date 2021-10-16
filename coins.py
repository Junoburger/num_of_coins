quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01


print("Please enter the amount of money to convert:")

dollars = str(input("# of dollars: "))
cents = str(input("# of cents: "))
set_amount = float(dollars + "." + cents)


def newQuotient(amount, denom):
    quotient = int(str(amount / denom).rsplit('.')[0])
    return quotient


def newDividend(amount, denom):
    remainder = round(amount % denom, 2)
    return remainder


num_of_quarters = newQuotient(set_amount, quarter)
remainder_for_quarters = newDividend(set_amount, quarter)
num_of_dimes = newQuotient(remainder_for_quarters, dime)
remainder_for_dimes = newDividend(remainder_for_quarters, dime)
num_of_nickels = newQuotient(remainder_for_dimes, nickel)
remainder_for_nickels = newDividend(remainder_for_dimes, nickel)
num_of_pennies = newQuotient(remainder_for_nickels, penny)
remainder_for_pennies = round(newDividend(remainder_for_nickels, penny))

print("The coins are",
      num_of_quarters,
      "quarters," if num_of_quarters > 1 else "quarter,",
      num_of_dimes,
      "dimes," if num_of_dimes > 1 else "dime,",
      num_of_nickels,
      "nickels," if num_of_nickels > 1 else "nickel,",
      num_of_pennies,
      "pennies," if num_of_pennies > 1 else "penny,")
