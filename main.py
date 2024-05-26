player_name = input("What is your name?")
holes_of_golf = input("Would you like to play 3 or 6 holes of golf?")
par = 3
course_par = 18
hole_1 = int(input("How many putts for hole 1? (par is 3)"))
hole_2 = int(input("How many putts for hole 2? (par is 3)"))
hole_3 = int(input("How many putts for hole 3? (par is 3)"))
hole_4 = int(input("How many putts for hole 4? (par is 3)"))
hole_5 = int(input("How many putts for hole 5? (par is 3)"))
hole_6 = int(input("How many putts for hole 6? (par is 3)"))
player_score = hole_1 + hole_2 + hole_3 + hole_4 + hole_5 + hole_6
total_score = player_score - course_par

if total_score > 3:
    print(f"Nice try,{player_name}... Your total score was: +{par}.")
elif total_score < 3:
    print(f"Great job,{player_name}! Your total score was: -{par}.")
elif total_score == 3:
    print(f"Good game,{player_name}. Your total score was: 0.")
