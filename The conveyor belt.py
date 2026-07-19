"""H1) An Amazon fulfilment centre has a conveyor belt with exactly 8 slots
numbered 0–7. Each slot holds one product. The warehouse manager needs to:
check what's at a slot, find a product, update a slot, and check if the belt is full.
The conveyor belt — fixed 8 slots"""

belt = [None] * 8

belt[0] = "desktop"
belt[1] = "pendrive"
belt[2] = "iphone"

print("Slot 1:", belt[1])

product = "pendrive"
if product in belt:
    print(product, "found at slot", belt.index(product))
else:
    print(product, "not found")

belt[1] = "iphone"
print("Updated Belt:", belt)

if None in belt:
    print("Belt is not full")
else:
    print("Belt is full")  
