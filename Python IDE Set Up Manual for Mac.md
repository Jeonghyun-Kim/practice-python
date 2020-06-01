# Python IDE Set Up Manual for Mac

This document is written by Jeonghyun Kim(kimjh@bawi.org).
You cannot share this manual without owner's permission.

## 0. Mac Shortcuts

> By pressing certain key combinations, you can do things that normally need a mouse, trackpad, or other input device.
In this section, we'll handle how to read and use shortcuts

Please keep these in your mind while following upcoming instructions.

- Command (or Cmd) ⌘
- Shift ⇧
- Option (or Alt) ⌥
- Control (or Ctrl) ⌃
- Caps Lock ⇪

Ex) ⌘C : Command + C, ⇧⌘T: Shift + Command + T

---

## 1. Python Installation

> Python3 must be installed on our computer in order to proceed with the class. Follow the steps below.

- Download python3 installation file from the official website.

    You can choose the version via this link.

    [Python Releases for Mac OS X](https://www.python.org/downloads/mac-osx/)

- Or just click this download link I prepared for you.

    [](https://www.python.org/ftp/python/3.8.3/python-3.8.3-macosx10.9.pkg)

- Execute the installation file. (ex. *python-3.8.3-macosx10.9.pkg*)

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled.png)

- Open Terminal. (⌘Space + ⌘T or just ⌘[hold] Space + T)

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%201.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%201.png)

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%202.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%202.png)

- Enter lines below to make sure Python3 is installed properly.

    ```bash
    % python3 --version
    ```

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%203.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%203.png)

    ```bash
    % pip3 --version
    ```

    Your versions(python3 and pip3) might be different from mine, but don't worry. It's not a big deal. Checking only 'major digit' is enough. (python: 3 and pip: 20)

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%204.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%204.png)

---

## 2. VS Code Installation

> There are several good text editors for programming,
We will use 'VS Code' for writing Python3 codes.

- Download VS Code from the official website.

    [Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/Download)

- Unzip(Open) the downloaded file. (ex. *VSCode-darwin-stable.zip*)

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%205.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%205.png)

- Drag and drop **Visual Studio Code.app** to Application Folder.

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%206.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%206.png)

- Now you can see **Visual Studio Code.app** on your Launchpad.

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%207.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%207.png)

---

## 3. Adding Python Extension in VS Code

> VS Code is just same as other text editors if you don't add extensions.
You should simply add one Python extension before we start.

- Open Visual Studio Code application and extensions tab as well. (⇧⌘X)

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%208.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%208.png)

- Search 'Python' and install the top extension.

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%209.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%209.png)

- Wait a moment(depends on network status, ~10m) for the installation to be completed.

- Open terminal in the VS Code(⌃` : Ctrl + `) and type the line below.

    ```bash
    % pip3 install pylint
    ```

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2010.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2010.png)

    ![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2011.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2011.png)

    if that code is not working, try this instead.

    %  sudo pip3 install pylint

- Open VS Code Palette(⇧⌘P) and type linter
and select "***Python: Select Linter***" **→ *pylint***

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2012.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2012.png)

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2013.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2013.png)

---

## 4. Run your first Python Program

> Now you're ready to start.
Let's start with the simple program.

- Create a new folder 'practice_python' to anywhere. (Desktop, Document or somewhere)

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2014.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2014.png)

- Open Folder in VS Code you created just before. (File - Open or ⌘O)

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2015.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2015.png)

- Add a file 'hello.py' to 'practice_python' directory.

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2016.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2016.png)

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2017.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2017.png)

- Type the code below and save. (⌘S)

    ```python
    print('Hello World!')
    ```

- Run the program. You can see 'Hello World!' in your console.

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2018.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2018.png)

---

## 5. (Optional) Using the Jupyter Notebook

> The Jupyter Notebook is an open-source(free) web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.
This tool makes you able to debug your code easily and get the results more friendly. Still, as stated above, it's not required.

- Type the line below. (Open terminal in the VS Code(⌃` : Ctrl + `) if it's not already opened)

    ```bash
    % pip3 install jupyter
    ```

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2019.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2019.png)

if that code is not working, try this instead.

%  sudo pip3 install jupyter

- Open VS Code Palette(⇧⌘P) again and type jupyter.
Select ***Python: Create New Blank Jupyter Notebook*** as well.

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2020.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2020.png)

- Save file inside of 'practice-python' folder as 'hello.ipynb'. (⌘S)

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2021.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2021.png)

- Type the code below again and run! (Press ⌃Enter) or (Click green play button)
It will work after the notification is on at the right bottom corner.

```python
print('Hello World!')
```

![Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2022.png](Python%20IDE%20Set%20Up%20Manual%20for%20Mac%20cb5cea2789a14cb68056c5f26c2235ca/Untitled%2022.png)

---

# * Congratulations! You're all set.