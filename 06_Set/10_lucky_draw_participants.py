"""
Question:
A company is organizing two Lucky Draw events.

Perform the following operations:

1. Find participants who registered
   for both events.

2. Find participants who registered
   for only one event.
"""

event_a = set(input().split())
event_b = set(input().split())

both_events = event_a & event_b

only_one = event_a ^ event_b

print(f"Participants in both events: {both_events}")
print(f"Participants in only one event: {only_one}")
