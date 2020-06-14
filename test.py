#(c.5)
def calculate_shipping(weight:int) -> int:
    "under 2 pounds, the rate is $2.00."
    if weight < 2:
        return 2
    "2 pounds but under 10 pounds, the rate is $5.00."
    if 2 <= weight < 10:
        return 5
    "packages of 10 pounds or more, the rate is $5.00 plus $1.50 per pound for each pound over 10."
    if weight >= 10:
        return 5 + (weight-10) * 1.5

assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50

print()
