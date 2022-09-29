# Have the user enter their investment amount and expected interest
inv_amount = input("Enter your investment amount: ")
exp_interest = input("Enter your expected interest: ")
# Each year their investment will increase by their investment + their investment + interest rate is

inv_amount = float(inv_amount)
# Print out the earnings after a 10 year period

exp_interest = float(exp_interest) * .01

for i in range(10):
    inv_amount = inv_amount + (inv_amount * exp_interest)

print("Investment after 10 years : {:.2f}".format(inv_amount))