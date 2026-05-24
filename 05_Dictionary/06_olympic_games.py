"""
Question:
You are organizing Olympic sports information
using a Python dictionary.

Perform the following operations:

1. Create an empty dictionary
   named olympic_sports.

2. Add:
   - two summer sports
   - two winter sports

3. Add two more sports to each season
   using different methods.

4. Print all dictionary items:
   - using .items()
   - using dictionary keys

5. Print only the sports lists.

"""

#1
olympic_sports = {}

#2
olympic_sports["Summer"] = ["Swimming", "Athletics"]
olympic_sports["Winter"] = ["Skiing", "Ice Hockey"]

#3
olympic_sports["Summer"].append("Gymnastics")
olympic_sports["Summer"].append("Cycling")

#3
olympic_sports["Winter"] += ["Snowboarding", "Figure Skating"]

print("Olympic Sports Dictionary:")
print(olympic_sports)

#4
print("\n--- Printing items (method 1: using .items()) ---")
for season, sports in olympic_sports.items():
    print(f"Season: {season} -> Sports: {sports}")

#4
print("\n--- Printing items (method 2: using keys) ---")
for season in olympic_sports:
    print(f"Season: {season} -> Sports: {olympic_sports[season]}")

#5
print("\n--- Only sports lists ---")
for sports in olympic_sports.values():
    print(sports)
