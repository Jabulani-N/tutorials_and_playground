# Creating a Windows Executable from a Python Script

**Contents**:
- [Creating a Windows Executable from a Python Script](#creating-a-windows-executable-from-a-python-script)
  - [Create a Virtual Python Environment (it's faster and easier than it sounds)](#create-a-virtual-python-environment-its-faster-and-easier-than-it-sounds)
    - [Why?](#why)
    - [How](#how)
    - [What did I just do?](#what-did-i-just-do)
  - [Create Executable via PyInstaller](#create-executable-via-pyinstaller)
    - [Have PyInstaller create your spec file](#have-pyinstaller-create-your-spec-file)
    - [Edit App name via spec file](#edit-app-name-via-spec-file)
    - [Credit Yourself](#credit-yourself)
    - [Create the Executable](#create-the-executable)



## Create a Virtual Python Environment (it's faster and easier than it sounds)

Ideally, you've already been using a virtual environment (venv) as you developed your app, but in case you haven't, I'll walk you through the process.

### Why?

"It works on my machine"

Those five words can herald hours of bugfixing.

This ounce of prevention can save hours of cure.


### How

to make (and use) an environment called `envNameHere`

1. open your terminal/Powershell and use

```
python.exe -m venv envNameHere
```

This will create a directory called `envNameHere`.

2. without changing directories, activate the environment via `.\example_env\Scripts\activate`.
   * you'll know it worked becuase you'll see this `(envNameHere)` before your working directory in the terminal:
     * ![screenshot of activated environment named 'example_env'](../../../img/tutorials/python/virtual%20ewnvironment/python%20environment%20activated.PNG)
     * you deactivate the environment via `deactivate` while the environment is activated. This will return you to normal.
       * You can freely reactivate and deactivate.
     * you can remove the environment by simply deleting the folder it created.

3. Now, we'll prepare the environment to run your script. Put `python.exe -m ` before your module commands (like pip) to run them in the context of your environment. For example, this is how you'll use `pip list` to see all your modules (you'll have nearly none installed by default, so this is also how you'll use pip to install the needed modules.)
   * ![pip list in py venv](../../../img/tutorials/python/virtual%20ewnvironment/python%20env%20pip.PNG)

4. If you're following the guide because this is your first venv, this is when you'll **test your script in the context of the environment** via `python.exe scriptName.py`. if your script runs on a `main.py`, you'll use `python.exe main.py` to use the python of the virtual environment. This is an ideal and uncontaminated testing environment.
    * Remember you'll be using `python.exe -m pip` for any modules you need to install to the venv.


### What did I just do?

The virtual environment you created has it's own installation of python, independant of your machine's version. This means you have an "even playing field" where any two machines running the same operating systme will behave identically when using this python this way. This also limits the potential for breaking your own personal Python installation.

Most relevant for creating executables, this also guarantees any python modules included are done intentionally, and use the version you want the application to use.


## Create Executable via PyInstaller

### Have PyInstaller create your spec file

### Edit App name via spec file

### Credit Yourself

### Create the Executable

"Pull the lever, Kronk!"



[def]: #how