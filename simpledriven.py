table = {
    ("A", "Dirty"): "Suck",
    ("B", "Dirty"): "Suck",
    ("A", "Clean"): "Right",
    ("B", "Clean"): "Left"
}

location = input("Location (A/B): ").upper()
status = input("Status (Clean/Dirty): ").title()

action = table.get((location, status), "Invalid Input")

print("Action:", action)
