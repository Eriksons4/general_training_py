#This is a basic calorie calculator

print("Today's date?")
td = input()
print("Breakfast calories?")
bc = int(input())
print("Lunch calories?")
lc = int(input())
print("Dinner calories?")
dc = int(input())
print("Snack calories?")
sc = int(input())
cpd = bc + lc + dc + sc
print("Calorie intake for " + str(td) + " " + str(cpd))