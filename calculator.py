# A simple program to calculate yearly interest

print("   +=+=+=+=+=+=+=+=+=+=+=+  ")
print(" \+=+=+=+=+Trojan0x=+=+=+=+/ ")
print("  \=========Built=========/   ")
print("   \=========This========/   ")
print("    \+=+=+=+=+=+=+=+=+=+/ ")

print(" ")
print(" ")

print(" Compound interest Calculator")
print(" ----------------------------")

print(" ")


years = int(input("How many years will you be saving: "))

principal = float(input("How much do you currently have in your account: "))

monthly_invest = float(input("How much money do you want to invest monthly: "))

print(" What is your estimated interest amount for the investment mentioned above?")
interest = float(input("Enter amount in decimal: (i.e 10% = 0.1)   >>> "))

print('')

monthly_invest = monthly_invest*12
total = 0

for i in range(0, years):
    if total == 0:
        total = principal
    
    total = (total + monthly_invest)*(1 + interest)

print("The total amount you will have in your account after {} years is = ".format(years) + str(total))
