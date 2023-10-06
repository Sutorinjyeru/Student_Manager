# Escreva um programa que permita selecionar
# um aluno aleatório de um arquivo txt.
# Permita que o programa adicione um aluno a lista.
# Permita que o programa remova
# um aluno da lista.

import PySimpleGUI as sg

from Layout import Menu
# Erros
# GUI
from manager import Manager

##aaa

def main():
    # Create list with the archive itens
    with open("Archive.txt") as file:
        allStudents = file.read()
        students = allStudents.split()
    # Program
    while True:
        event, values = Menu.window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'Choose a random student':            
            random_value = Manager.random_student()
            Menu.window['textbox2'].Update(random_value)
        if event == 'Add Student':
            new_student = Manager.add_student(students, values[0])
            Menu.window['textbox'].Update(new_student, values[0])
        if event == 'Remove Student':
            anti_student = Manager.remove_student(students, values[1])
            Menu.window['textbox'].Update(anti_student, values[1])
    Menu.window.close()


if __name__ == "__main__":
    main()
