"""
Question:
You are managing pets at a veterinary clinic.

Perform the following operations:

1. Add a new patient:
   - Sugar
   - horse
   - age 4.

2. Print all animal names:
   - using a loop through elements
   - using a loop through indices

3. Add clinic status information
   indicating all animals are currently
   in the clinic.
   
"""

pets = [
    {"name": "Toby", "animal type": "dog", "age": 2},
    {"name": "Kitty", "animal type": "cat", "age": 5},
    {"name": "Tiki", "animal type": "parrot", "age": 1}
]
#1
pets.append(
    {"name": "Sugar", "animal type": "horse", "age": 4}
)
print("After adding new patient:")
print(pets)

#2 [using a loop through elements]
print("\nAnimal names (using elements):")
for pet in pets:
    print(pet["name"])

#2 [using a loop through indices]
print("\nAnimal names (using indices):")
for i in range(len(pets)):
    print(pets[i]["name"])

#3
clinic_status = "All animals are currently in the clinic."
print("\nAfter adding clinic status:")
print(pets)
print("Clinic Status:", clinic_status)
