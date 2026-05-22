"""
Question:
You are managing new T-shirts in a clothing store.
Perform the following operations:
1. Create a dictionary with:
   - Color
   - Size
   - Neck Type
2. Add:
   - Quantity using direct assignment
   - Logo Color using update()
3. Add:
   - Sold quantity
4. Update remaining stock using:
   Quantity = Quantity - Sold
   
"""

#1
tshirt = {
    "Color": "Red",
    "Size": "M",
    "Neck Type": "Round"
}

print("a. Initial T-shirt information:")
print(tshirt)

#2
tshirt["Quantity"] = 25
tshirt.update({"Logo Color": "Blue"})
print("\nb. After adding quantity and logo color:")
print(tshirt)

#3
tshirt["Sold"] = 20
print("\nc. After recording sales:")
print(tshirt)

#5
tshirt["Quantity"] = tshirt["Quantity"] - tshirt["Sold"]
print("\nd. After updating remaining quantity:")
print(tshirt)
