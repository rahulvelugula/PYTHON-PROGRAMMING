"""
Question:
Write a Python program to compare
two DNA sequences using sets.

Perform the following operations:

1. Input two DNA sequences.

2. Find:
   - Common nucleotides
   - Nucleotides unique to first sequence
   - Nucleotides unique to second sequence

3. Find missing nucleotides
   from each sequence using:
   {A, T, C, G}

4. Display all results

"""

dna1 = input()
dna2 = input()
set1 = set(dna1)
set2 = set(dna2)

bases = {"A", "T", "C", "G"}

common = set1 & set2
unique1 = set1 - set2
unique2 = set2 - set1
missing1 = bases - set1
missing2 = bases - set2


print(f"Common nucleotides: {common}")
print(f"Unique to first sequence: {unique1}")
print(f"Unique to second sequence: {unique2}")
print(f"Missing from first sequence: {missing1}")
print(f"Missing from second sequence: {missing2}")
