import PySimpleGUI as sg
import speech_recognition as sr

#styling
sg.theme('DarkTeal7')
sg.set_options(font=('San Serif', 14))

#layout of GUI
layout = [[sg.Text("Speech Recogniser")]], [sg.Multiline(size=(70,20), key="-OUTPUT-"), [sg.Button("Record", border_width=10), sg.Button("Exit", border_width=10)]]

window = sg.Window("Speech Recogniser", layout)

#event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Record":
        r= sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            window["-OUTPUT-"].update(text)
        except sr.UnknownValueError:
            window["-OUTPUT-"].update("Could not understand. Please Try again")
        except sr.RequestError as e:
            window["-OUTPUT-"].update(f"Error: {e}")

window.close()
