# Creating a Windows Executable from a Python Script

**Contents**:
- [Creating a Windows Executable from a Python Script](#creating-a-windows-executable-from-a-python-script)
  - [Create a Virtual Python Environment (it's faster and easier than it sounds)](#create-a-virtual-python-environment-its-faster-and-easier-than-it-sounds)
    - [Why?](#why)
    - [How](#how)
    - [What did I just do?](#what-did-i-just-do)
  - [Create Executable via PyInstaller](#create-executable-via-pyinstaller)
    - [Have PyInstaller create your spec file](#have-pyinstaller-create-your-spec-file)
      - [Note](#note)
    - [Edit App name via main.spec file](#edit-app-name-via-mainspec-file)
    - [Credit Yourself via version.rc file](#credit-yourself-via-versionrc-file)
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

The virtual environment you created has it's own installation of python, independant of your machine's version and installed modules. This means you have an "even playing field" where any two machines running the same operating systme will behave identically when using this python this way. This also limits the potential for breaking your own personal Python installation.

Most relevant for creating executables, this also guarantees any python modules included are included intentionally, and use the exact version you want the application to use.


## Create Executable via PyInstaller

Now that you have a Virtual Environment (venv) up and running your script without a hitch, you can begin creating the excecutable file itself using PyInstaller. Be sure you've installed it to your venv using `python.exe -m pip install pyinstaller`

### Have PyInstaller create your spec file

Rather than put the work into structuring this yourself, we'll have PyInstaller do it for us: `python.exe -m PyInstaller scriptName.py` will create an executable with default values, and it may actually run if absolutely everything is self-contained within the single script file. We're not done yet, however. It will also create a file called `main.spec`. That's how we'll tailor the created executable to our needs.

#### Note

You might consider renaming `main.spec`, as anytime you run pyinstaller from your `main.py` file, it'll create main.spec with default values, overwriting your own, if it has the same name.

### Edit App name via main.spec file

Your newly created `.spec` file will have a structure similar to, but not identical to, <details>
<summary>this one</summary>


![top half](../../../img/tutorials/python/PyInstaller/spec%20file%20-%20analysis%20(top).PNG)
![bottom half](../../../img/tutorials/python/PyInstaller/spec%20file%20-%20pyz,%20exe.PNG)
</details>

To name your app, you'll navigate to the `exe =` section and create or change the `name=''` line to `name='name_of_your_app'`

### Credit Yourself via version.rc file

![credits in properties](../../../img/tutorials/python/PyInstaller/credits%20in%20properties.png)

To populate the details of your app, we'll use a `version.rc` file. The idea is similar to that of the `main.spec` file, but this one is for Properties Details. I use [this](../../demonstrations/syntax/python/PyInstaller/version.rc) as a template.

Some notable fields are

When you've filled in the information you want, you'll add the `.rc` file to your application by adding `version='version.rc_file_name'` to your `.spec` file, within the `exe = EXE(` section.

For example:
![spec file with version file linked](../../../img/tutorials/python/PyInstaller/spec%20file%20version%20line.PNG)

### Create the Executable

![do the thing!](../../../img/zhu-li,%20do%20the%20thing.gif)

Now we're ready to create the executable. Have PyInstaller run the spec file, in the context of your venv, with `python.exe -m PyInstaller spec_file_name.spec`.

Give it time to work, and that's your python app built and personalized!
