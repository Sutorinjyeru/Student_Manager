import PySimpleGUI as sg

from manager import Manager as Mg


class Menu:
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    # Choose_Button = sg.Button(
    #     'Choose a random student', enable_events=True)
    # Add_Button = sg.Button('Add student', enable_events=True)
    # Remove_Button = sg.Button('Remove Student', enable_events=True)

    layout = [[sg.Text('Hello User, make your choice!')],
              [sg.Multiline(size=(30, 5), key='textbox', default_text=Mg.simple_list())],
              [sg.Button('Chosse a random student', enable_events=True)],
              [sg.Multiline(Mg.random_student())],
              [sg.Text('Type the name you want to add.'), sg.InputText()],
              [sg.Button('Add Student', enable_events=True)],
              [sg.Text('Type the name you want to remove.'), sg.InputText()],
              [sg.Button('Remove Student', enable_events=True)]]


    # Create the Window

# Event Loop to process "events" and get the "values" of the inputs
    window = sg.Window('Student Manager', layout, size=(700, 600))
    # window2 = sg.Window('Page2', layout2, size=(700, 600))
    # window3 = sg.Window('Page2', layout3, size=(700, 600))
    # window4 = sg.Window('Page2', layout4, size=(700, 600))
