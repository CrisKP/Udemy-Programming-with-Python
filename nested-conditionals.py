#Nested if statements
total = 800
customer = "retail"

if customer == "retail":
    if total > 0 and total < 100:
        discount = 0
    elif total >= 100:
        discount = 0.1
elif customer == "wholesale":
    if total > 0 and total < 500:
        discount = 0.2
    else:
        discount = 0.15
else:
    discount = 0

print(discount)
