import PySimpleGUI as sg

from manager import Manager


class Menu:
    sg.theme('DarkAmber')   # Add a touch of color

    layout = [[sg.Text('Hello User, make your choice!')],
              [sg.Multiline(size=(30, 10), key='textbox', default_text=Manager.simple_list(), autoscroll= False)],
              [sg.Button('Choose a random student', enable_events=True)],
              [sg.Multiline(size=(30,1), default_text="", key='textbox2')],
              [sg.Text('Type the name you want to add.')],
              [sg.InputText()],
              [sg.Button('Add Student', enable_events=True)],
              [sg.Text('Type the name you want to remove.')],
              [sg.InputText()],
              [sg.Button('Remove Student', enable_events=True)]]

#[sg.Multiline(size=(30, 10), key='textbox', default_text=Manager.simple_list())]
    window = sg.Window('Student Manager', layout, size=(700, 600))
    #window.Update(values[0])
