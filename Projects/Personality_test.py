#beginning
Xmas_points = 0
Grinch_points = 0

#middle
answer = input ("what is the xmas song? ____ the red nosed raindeer?")
if answer == "Rudolph" or "rudolph": 
    Xmas_points += 1
else:
    Grinch_points += 1


answer = input("Who is the man in red and white with a hat and eats cookies and milk?")
if answer == "Santa" or "santa":
    Xmas_points += 1
else:
    Grinch_points += 1


answer = input("What does santa use to fly around on his sleigh?")
if answer == "Reindeer" or "reindeer":
    Xmas_points += 1
else:
    Grinch_points += 1


answer = input("Where is santa's workshop")
if answer == "North pole" or "north pole":
    Xmas_points += 1
else:
    Grinch_points += 1


answer = input("Who makes santa's presents?")
if answer == "Elves" or "elves":
    Xmas_points += 1
else:
    Grinch_points += 1

#end
if Xmas_points > Grinch_points:
    print("You like CHRISTMAS")
elif Grinch_points > Xmas_points:
    print("you are big green mean man")
exit(2)