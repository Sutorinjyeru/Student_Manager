import PySimpleGUI as sg
from Class import Manager as Mg

class Menu:
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    Choose_Button = sg.Button(
        'Choose a random student', enable_events=True)
    Add_Button = sg.Button('Add student', enable_events=True),
    Remove_Button = sg.Button('Remove Student', enable_events=True)

    layout = [[sg.Text('Hello User, make your choice!')],
              [Choose_Button, Add_Button, Remove_Button],]

    layout2 = [[sg.Text(Mg.random_student())]]

    layout3 = [[sg.Text('Type the name you want to add.'), sg.InputText()],
               [sg.Button('Enter', enable_events=True)]]

    layout4 = [
        [sg.Text('Type the name you want to remove.'), sg.InputText()],
        [sg.Button('Enter', enable_events=True)]]
    # Create the Window

# Event Loop to process "events" and get the "values" of the inputs
    window = sg.Window('Student Manager', layout)
    window2 = sg.Window('Page2', layout2)
    window3 = sg.Window('Page2', layout3)
    window4 = sg.Window('Page2', layout4)
