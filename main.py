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
            Manager.random_student()
        if event == 'Add Student':
            newvalue = Manager.add_student(students, values[1])
            Menu.window['textbox'].Update(newvalue, values[1])
        if event == 'Remove Student':
            Manager.remove_student(students, values[2])
            Menu.window['textbox'].Update(values[2])
    Menu.window.close()


if __name__ == "__main__":
    main()
