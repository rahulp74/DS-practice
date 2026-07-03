"""The E-Commerce Price Filter (First occurrence ≥ target)

You're on Flipkart. You filter products:
"Show me laptops priced ₹50,000 or above."
Products are sorted by price.
Flipkart must find the first product ≥ ₹50,000 — a classic binary search variant 
called lower bound."""
prices = [1000, 300, 5000, 60000, 85000, 95000]
t= 50000

low = 0
high = len(prices) - 1
a= -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= t:
        a= mid
        high = mid - 1
    else:
        low = mid + 1

if ans != -1:
    print("First product >= ₹50000:", prices[a])
    print("Index:", a)
else:
    print("No  found")
