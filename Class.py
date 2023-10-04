from random import choice


class Manager:
    @staticmethod
    def random_student():
        with open("Archive.txt") as file:
            allStudents = file.read()
            students = allStudents.split()
            return choice(students)

    @staticmethod
    def add_student(sList: list, var: str):
        # Remove All
        with open("Archive.txt", "w") as file:
            file.write("")
        # Create new
        with open("Archive.txt", "a") as file:
            sList.append(var)
            for name in sList:
                file.write(name+"\n")

    @staticmethod
    def remove_student(sList: list, var: str):
        with open("Archive.txt") as file1:
            items = file1.read()
            newList = items.split()
        # Remove All
        with open("Archive.txt", "w") as file:
            file.write("")
        # Create new
        try:
            with open("Archive.txt", "a") as file:
                sList.remove(var)
                for name in sList:
                    file.write(name+"\n")
        except ValueError:
            print("Name not in list, try again. ")
            with open("Archive.txt", "w") as file1:
                for i in newList:
                    file1.write(i+"\n")
    # @staticmethod
    # def change_to_page_2():
