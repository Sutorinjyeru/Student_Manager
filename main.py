# Escreva um programa que permita selecionar
# um aluno aleatório de um arquivo txt.
# Permita que o programa adicione um aluno a lista.
# Permita que o programa remova
# um aluno da lista.

import PySimpleGUI as sg
# Erros
# GUI
from Class import Manager as Mg
from Layout import Menu


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
            Menu.window.close()
            event, values = Menu.window2.read()
        if event == 'Add student':
            Menu.window.close()
            event, values = Menu.window3.read()
            Mg.add_student(students, values[0])
        if event == 'Remove Student':
            Menu.window.close()
            event, values = Menu.window4.read()
            Mg.remove_student(students, values[0])

    Menu.window.close()


if __name__ == "__main__":
    main()
