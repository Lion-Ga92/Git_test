from Git_test.Classes import List

print("Welcome to the Git test prototype task list app")
print("input your answers as 'yes' or 'no' in lowercase letters")

day_one = List("Cut corn", "Peel corn", "Take out trash", "Wash pots")
day_two = List("Thaw out meats", "Wash corn husks", "Clean pots", "Clean cart")

print("Your day one tasks are...")
day_one.list_tasks()
print("Your day two tasks are...")
day_two.list_tasks()