"""
nmcl-nmap.py 
A GUI for nmap.
"""

# Imports needed Libraries
import PySimpleGUI as ps
import os


# Sets Themes (change themes to fit your preference), refer to PySimpleGUI docs for more on themes
ps.theme('DarkBlue')


# Defines layout for window with PySimpleGUI
layout = [ [ps.Text('Nmap - NMCL', justification='center')],
           [ps.Text('Ip/Address to Scan:'), ps.InputText(key='-IP-')],
           [ps.Button('Scan')],
           [ps.Text('Results: ', key='-RES-')],
]

# Creates the Window using 'layout'
windowroot = ps.Window('Nmap - NMCL', icon='nmcl.png').Layout(layout)

ip = '8.8.8.8' # pings google if no ip is submitted

# While loop for inputs
while True:
    event, values = windowroot.read()
    if event == ps.WIN_CLOSED: # Checks to see if window is closed
        break
    if event == 'Scan': # Checks to see if button is pressed.
        ip = values['-IP-'] # Grabs text from InputText
        os.system('nmap -oN nmapres.txt ' + str(ip)) # Executes nmap and saves results to 'nmapres.txt'
        f = open('nmapres.txt', 'r')
        res = f.read() # Opens saved txt file in read mode
        windowroot['-RES-'].update('Results: ' + str(res)) # Updates results text with text from .txt file.
        f.close()