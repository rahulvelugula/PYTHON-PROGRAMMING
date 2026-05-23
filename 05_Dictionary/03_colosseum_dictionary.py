"""
Question:
You are organizing information about the Colosseum
using a Python dictionary.

Perform the following operations:

1. Create a dictionary with:
   - Location
   - Construction Years
   - Type

2. Update construction details:
   - Remove "Construction Years"
   - Add "Construction Start Year"
   - Add "Construction End Year"

3. Calculate:
   - Years taken to build the Colosseum
   - Years passed since construction started
   
"""

from datetime import datetime
colosseum = {
    "Location": "Rome",
    "Construction Years": "70–80 AD",
    "Type": "Amphitheater"
}

print("a. Initial Colosseum information:")
print(colosseum)

# Remove old construction years
del colosseum["Construction Years"]

# Add updated construction details
colosseum["Construction Start Year"] = 72
colosseum.update({"Construction End Year": 80})
print("\nb. After updating construction details:")
print(colosseum)

# Years taken to build
years_taken = (
    colosseum["Construction End Year"]
    - colosseum["Construction Start Year"]
)
print(f"\nc. It took {years_taken} years to build the Colosseum.")

# Years passed since construction started
current_year = datetime.now().year
years_passed = current_year - colosseum["Construction Start Year"]
print(
    f"d. {years_passed} years have passed since its construction started."
)
