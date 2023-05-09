# DesktopApp_Qt_Example_Production

Development Environment: root directory and run python Main.py

My Development Python Version (Backend): Python 3.9.2

Qt Design (Windows Qt Designer) -Frontend : ui files

___________________________________________________________________________________

Compile command into exe: pyinstaller --onefile Main.py

___________________________________________________________________________________

However, the line of code requires load the UI files therefore need to copy Design folder beside EXE file where stores the backend logic and UI
frontend will be accessed by the public. I guess doesnt matter?

___________________________________________________________________________________

Therefore production program can be found in dist/Main

All you need is copy dist/Main to run Python QT project (ready to sell to the customer, this is a simple example only, for reference later on)