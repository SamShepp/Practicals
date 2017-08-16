"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

#Sales Bonus
sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus is $", bonus, sep='')

#Original
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
if score < 50:
    print("Bad")

#Remake
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
