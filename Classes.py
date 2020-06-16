class List:
    def __init__(self, task1, task2, task3, task4):
        self.task1 = task1
        self.task2 = task2
        self.task3 = task3
        self.task4 = task4

    def list_tasks(self):
        print("1: " + self.task1)
        print("2: " + self.task2)
        print("3: " + self.task3)
        print("4: " + self.task4)


    def check_for_tasks(self):
        complete_string = ""
        complete_string += input("Name and date: ")
        complete_string += "\n"
        print("Have you completed " + self.task1 + "?")
        comp_task1_check = input("Yes or no: ")
        if comp_task1_check == "yes":
            print("You completed, " + self.task1)
            complete_string += "You completed " + self.task1 + "!" + "\n"
        elif comp_task1_check == "no":
            print("You still need to complete " + self.task1 + "\n")
            complete_string += "You still need to complete " + self.task1 + "\n"
        else:
            print("Response not valid")
            return

        print("Have you completed " + self.task2 + "?")
        comp_task2_check = input("Yes or no: ")
        if comp_task2_check == "yes":
            print("You completed, " + self.task2)
            complete_string += "You completed " + self.task2 + "!" + "\n"
        elif comp_task2_check == "no":
            print("You still need to complete " + self.task2 + "\n")
            complete_string += "You still need to complete " + self.task2 + "\n"
        else:
            print("Response not valid")
            return

        print("Have you completed " + self.task3 + "?")
        comp_task3_check = input("Yes or no: ")
        if comp_task3_check == "yes":
            print("You completed, " + self.task3)
            complete_string += "You completed " + self.task3 + "!" + "\n"
        elif comp_task3_check == "no":
            print("You still need to complete " + self.task3 + "\n")
            complete_string += "You still need to complete " + self.task3 + "\n"
        else:
            print("Response not valid")
            return

        print("Have you completed " + self.task4 + "?")
        comp_task4_check = input("Yes or no: ")
        if comp_task4_check == "yes":
            print("You completed, " + self.task4)
            complete_string += "You completed " + self.task4 + "!" + "\n"
        elif comp_task4_check == "no":
            print("You still need to complete " + self.task4 + "\n")
            complete_string += "You still need to complete " + self.task4 + "\n"
        else:
            print("Response not valid")
            return

        task_file = open("task_list2.txt", "a+")
        task_file.write(complete_string)
