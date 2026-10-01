# AI Engineering Fellowship

## Setup & Tools

### Git & Github
Watch this: https://www.youtube.com/watch?v=a9u2yZvsqHA
Create readme for all notes
Ensure to have the .gitignore in root and the pertinent internal text
This ignored both variations.

```
venv/
.venv/
.env
__pycache__/
*.pyc
```

#### .gitignore explained
`venv/` dir is the old school/orthodox folder for virtual environments

`.venv/` dir is the modern convention. By adding the dot, it hides from view in Unix based systems.

`.env` file often holds API keys, configuration settings or sensitive data like database passwords, secret keys for authentication sessions, server port numbers, or debug mode toggles

`__pycache__/` Directory:
This is simply the folder that Python 3 automatically creates to neatly organize and store all of those .pyc files in one place, rather than scattering them throughout your project directory.

`*.pyc` files:
When you run a Python script, Python translates your human-readable code into a lower-level format called bytecode, saving it with the .pyc extension. This allows the computer to execute the code faster on subsequent runs without having to re-translate it from scratch.



### Python
Python vs VS Code Installation Steps
Python installation

Download the Python installer from https://www.python.org/downloads/ 

Choose a stable version in 3.12 or 3.13
Choose the  installer
Complete the installation
Check the installation
Command Prompt: python --version to see the version installed
Command Prompt: where Python to check the path installed


### VSCode
VSCode Installation:
Download the VSCode installer from https://code.visualstudio.com/download for your machine.
Complete the installation
Ctrl + Shift + P → Python: select interpreter → Choose the Python installed in your PC
Install extensions: Go to the extension tab and install the following
Python
Python Debugger
Jupyter

### Environment setup in Terminal
Check python setup
>`which python3`
>`Python3 --version`
>`git --version`

>`python -m venv myenv`
>`source myenv/bin/activate`

>`pip install <package1,package2,...>`

Work on project
>`python app.py`
Done working
> `deactivate`

In directory env is needed
`python3 -m venv S01_env`
`source S01_env/bin/activate`
To verify, the python version is pulled from the env just active and the terminal will show (env name)
`which python3` 

`pip freeze`
`pip list`
`pip freeze > requirements.txt`
`pip install -r requirements.txt`

View what in requirements
`vi requirements.txt`


# Python on Mac & Win
Different setup has different commands
Mac/Linux has a System Python->Global/User->vEnv.
User python uses python3, pip3
Windows has a Global/User-> vEnv , only.
User python uses python, pip, py

Virtual Environment use python and pip on both. More simple. We c

The protocol of new projects, we create a new folder and virtual environment.
- Unix we use python3 -m venv .venv
- WIN  we use py -m venv .venv

Standard practice is to call it .venv or venv
Create a new virtual environment for each new project

Active when using
- Unix we use: source .venv/bin/python
- WIN  we use: .venv\Scripts\activate

The (venv) in terminal will indicate its active.

Activate is only persistent in one window. If opening another temrinal window, it will need to be activated again.

Activating the vENV focuses instead of broad view in terminal. Think locked-in or linked to the project.

Activate and Deactivate multiple times a day.
pip install [package name]
pip uninstall [package name]

# Warnings
Do not mess with your vEnv directly. 
Do not put any files in it.
Only use pip to install/uninstall

streamlit run has its own commands. Other packages have their own commands.

we use the requirement.txt to communicate the env instead of sending the virtual environment. We make sure they are both at the same level. 
Root
|_.env
|_requirements.txt
|_example.py

When receiving requirements file:
1.Create the virtual environment
2.Activate the vEnv
3.install using `pip install -r requirements.txt`
 -r means repeate

To send requirements file:
pip freeze > requirements.txt

close terminal window or deactivate
its okay to delete .env if completely done and ready to hybernate the project. Use pip freeze before deleting the folder

# Troubleshoot
Command not found/import error inside Virtual Environment
! Common Mistake: people forget to install packages before use
Problem: You created and activate your virtual environment, but some command is not working (command not found error)
OR some package import is throwing an error?
Answer: You forgot to install that package! What commands can you use to install it?

Do not forget to activate your virtual environment.
Even pro's repeat this mistake!
Make a habit to check these two:
Virtual environment created?
Virtual environment activated?

Check:
• Did you create virtual environment?
• Are you in the correct folder?
• Run `ls` command to check: does virtual environment folder exists?

Read the documentation:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
Seriously, open the link and scroll down at least once.

# -- END --