player_name = input("What is your name?")
par = 3
course_par3 = 9
course_par6 = 18
holes_of_golf = input("Would you like to play 3 or 6 holes of golf?")
hole_1 = int(input("How many putts for hole 1? (par is 3)"))
hole_2 = int(input("How many putts for hole 2? (par is 3)"))
hole_3 = int(input("How many putts for hole 3? (par is 3)"))
hole_4 = int(input("How many putts for hole 4? (par is 3)"))
hole_5 = int(input("How many putts for hole 5? (par is 3)"))
hole_6 = int(input("How many putts for hole 6? (par is 3)"))

for h in holes_of_golf:
    if h == 3:
        print(hole_1)
        print(hole_2)
        print(hole_3)
        break

player_score3 = hole_1 + hole_2 + hole_3
player_score6 = hole_1 + hole_2 + hole_3 + hole_4 + hole_5 + hole_6
total_score3 = player_score3 - course_par3
total_score6 = player_score6 - course_par6

if total_score3 > 3:
    print(f"Nice try,{player_name}... Your total score was: +{par}.")
elif total_score3 < 3:
    print(f"Great job,{player_name}! Your total score was: -{par}.")
elif total_score3 == 3:
    print(f"Good game,{player_name}. Your total score was: 0.")

if total_score6 > 3:
    print(f"Nice try,{player_name}... Your total score was: +{par}.")
elif total_score6 < 3:
    print(f"Great job,{player_name}! Your total score was: -{par}.")
elif total_score6 == 3:
    print(f"Good game,{player_name}. Your total score was: 0.")
