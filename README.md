# Learning Python

This is my readme file. It is for documenting my programming knowledge.

## April 3rd

Beege and I installed several things and configured them.
First we installed a version manager (not a version control system) called asdf
Then we installed vim and python
This required a number of developer libraries for support of python
We created a project directory and a sub directory with mkdir
Then made main.py file using touch
We checked permissions with ll (alias of ls -l)
Then we changed permissions to allow (+) the user(u) to execute(x) (chmod u+x)
    chmod u+x file.name
Entering the file with vim ./main.py
creating a shebang command (#!) then listing the directory path (/usr/bin/env) and file to use as the executable (python). This allows the system to search for the python executable whereever it is.
Wrote hello world (print("hello world")
exited with :wq (w for write to file, q for quit)

## April 10th
When opening a terminal in the gui the .profile is not read. .bashrc is read instead.
In visual studio, a white dot means there are unsaved portions of the file

## April 17th
learning git
To include a message use git commit -m "message"
To set a username git commit user.name "TheName" (add --global to set it globally)
To set an email git commit user.email "asdf@email.com" (also can be global)
git status shows the status of the files to be committed
git add filename.filetype will add a file to be committed
git log displays the history of a file or the git repo
git branch displays the current branch
get checkout -b branchname is a cmd to make a new branch (git branch can do it, but won't move you there)
git checkout moves to a new branch, -b allows it to make a new branch if it doesn't exist
git merge branchname will merge it back into master (this should be run from the branch you want to merge into. Thus run it while in master.)
git tag -a name -m (-a adds, -m adds a message)
git tag -n will display the tag messages. -n#, where # is a number will show # lines of the message.

## April 20th and 21st
I have begun creating small programs for practice with reading files and selecting random elements.

## April 24th
I have been creating a number of small projects.
Dependencies are pieces of code that other people have written that provide utility or reduce reinventing the wheel.
python uv
python dependencies are managed by tools like 'pip' or 'python uv'
uv also handles python versions
uv init . (Tells uv to initialize a new project in the current folder [. is current folder])
uv init name allows it to create a new project folder with all the files needed. When we have a project, it will not do this.
This sets up a pyproject.toml file which tracks project configuations and makes transfering between computers much easier.
It also tracks which dependencies you need.
uv add allows adding a dependency to the project. This adds it to a virtual environment, instead of it's site packages that are global.
venv files create essentially a full copy of python.
uv.lock controls the version of a dependency. It prevents tampering with dependencies.
Do not git .venv (it is of no use to you or others). The point of pyproject.toml is to allow recreating a venv
gitignore will ignore each file name in a new line

VSCode has a git interface
Anything under "changes" is not being committed

ACTIVATING A VIRTUAL ENVIRONMENT IS CRITICAL
source .venv/bin/activate
When activated properly it will add (foldername) at the start of the terminal path

When running a program and an error occurs, we get red or purple text.

git add -A adds all files in folder