# A simple Python UDP Socket based Calculator

Welcome, this is an example project of the class(CPT 411) assignment,plus instructions and explanations on how to get started with git and get your code on Github.

if you notice any errors or if there's any confusing parts please point it out, that would be much appreciated.

__Please note that this is just a small tutorial to help you get the Git part done, You should read more about Git on Your free time to learn more about how to use it in your projects.<br> There are some links to very good resources for learning both python and git at the bottom of this page.__

# Table of Content

- [What is Git?](#what-is-git?)
- [How does Git work?](#how-does-git-work?)
- [What is Github?](#what-is-github?)
- [How to get Git](#how-to-get-git)
- [Getting Started with Git](#getting-started-with-git)
- [How to get your Code on Github](#how-to-get-your-code-on-github)
- [Links to Recommended tutorials and books](#more-information)

# Introduction

## What is Git?
Git is a type of __version control system__(VCS), it is used for tracking the changes that are made to computer files, and coordinating work on those files among many people.

__whats is a version control system(VCS)__:
It is a  tools that helps a software team manage changes to source code over time.

It is primarily used for __source code management (SCM - as in git-scm.com)__ in software development, but it can be used to keep track of changes in any set of files.

__Important Use__:

It keeps track of every change made to the code in a special kind of database. If a mistake is made, developers can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.


__what is a repo?__:
A __repository__, known as a __"repo"__ for short, simply means a storage location.

__what is a git repo__:
A __Git repository__ is a virtual storage of your project. It allows you to save versions of your code, which you can access when needed. 


__what is a remote repo?__:

A remote repo simply refers to a repository that is hosted on another computer/server, or hosting service such as Github, and Bitbucket.

__in git your repo is the .git folder(it's a hidden folder) in your project folder(working directory) it is called a local repo because it's located on your (local)machine__

### How does Git work?

Git is an example of a DVCS (Distributed Version Control System). Distributed means that everybody's copy of the project is also a repository that contains the full history of all changes.

There are three major parts of a git project.

- __The Working Directory__: your project folder
- __The Staging Area__: a list of files that you want git to keep track of, all changes made to files in  the staging area can be save to your repo by committing them
- __The Repository__: A special database that can save snapshots of all the files and folders in the staging area, which can later be restored.


## What is Github?
GitHub is a web-based hosting service for version control using git. It is mostly used for computer code. It offers all of the distributed version control and source code management functionality of Git as well as adding its own features.

# Git Basics

## How to get Git
To install git on your computer, follow the following instructions for your Operating System

- __Linux and Unix__: you can install Git on Linux using the preferred package manager of your Linux distribution. You can find installations instructions for your linux distribution [here](https://git-scm.com/download/linux)
- __Windows__: Click [this link](https://git-scm.com/download/win) to download the latest version for Windows.

- __Mac OS__: Click [this link](https://git-scm.com/download/mac) to download the latest version for Mac OS.

## Getting Started with Git
Once you've installed git, to check whether it was properly installed, type `git --version`in your command line or terminal(by terminal I am also referring to git bash, if you chose to use it), this is supposed to show you which version of git you have installed.

If you get an error,try installing git using the links above.

- __what to do after installing__: After installing git, you need to do some important configuration, so open a command line or terminal(or git bash if you selected it).
	+ set your email address, using:
		
```
git config --global user.email "myemail@email.com"
```
replace 'mymail@email.com' with your email address

+ set your user name, using:
	
```
git config --global user.name "myusername"
```

+ replace 'myusername' with a username of your choosing.

- __create(initialize) a repo__: you can turn any folder/directory on your computer to a git repository by navigating to the folder in your command line/terminal/ git bash and enter the following:

```
git init
```
- __copy(clone) a repo__: cloning a repository means exactly what it suggests, it creates a copy of a remote repository to your computer, to do this you need the URL of the repo you want to clone.

**For example** to clone this repo, navigate to the folder you would like to clone it into through your command line or Terminal(Bash), and use the `git clone` command  like this:

	git clone https://github.com/dbugshe2/simple-python-udp-socket-calculator

and it will create a folder called `simple-python-udp-socket-calculator` containing all the files in this repo.


- __working with remote repos__: a remote repo is simply a copy of a local repo, on another computer, and one project can have many different remote repos.
If you `clone` a remote repo, then the cloned repo is added by default as one of your remote repos.

## How to get your Code on Github
Suppose you have a folder `work` containing your programs and you would like to put it on GitHub. You can make this happen by following the steps below

__(When I say command line depending on your os or setup this might mean your 'cmd' or 'Terminal' or 'git bash')__

1. __install git__ You must have git installed (you can find links above).

2. __initialize(create) a local repo__: To create a local repo you should
	- open a command line, and navigate to the `work`  folder you can do this by:
		- typing `cd` followed by space, then drag and drop the folder on the command line window, then hit 'enter'
	- then make the folder a git repo by typing the command:
		
``` 
git init
```
3. __add your files to your git staging area__: this simply means you want git to start keeping track of the files, you can tell git to keep track of your files by typing:

```
 git add <file1 name> <file2 name>
```

or you can simply use `.`(period) to add all the files in that folder using:

```
git add .
```
now git will keep track of all the changes you make to those files from this point onwards.

4. __Prepare to commit your changes__: so now that you have git tracking all your changes, and lets say you've made some progress, or you've finished the program and you've tested it. now you want to save(commit) this current working version of your program to your repo. You add them to the list of changes to be committed, using the same add command.

``` 
git add <file1 name> <file2 name>
```

5. __Save all your tracked changes(so far)__:
Time to commit the changes, for this we use the `commit` command.

``` 
git commit -m "create a calculator app"
```

what this does is that it saves a snapshot(commit) of all the files that you're tracking, so that you can later go back to this snapshot or even send it to another repository.

__the text in quotes after the `-m` part of the command is the 'commit message' this should be a description of the changes you have made so far.__

6. __Get a Github account__ Sign-up on GitHub if you haven't. [Click here to got to the registration page](https://github.com/join) (Open this in another tab)

7. __Create a github repo__: create a repo by following these steps.
	- click on the `+` icon at the top right and select 'new repository'<br>
![Image](new-repo.png?raw=true)
	- On the new repo page enter a name for the repo, separating each word in the name with a hyphen `-` (__leave all other option the way they are__)<br>
![Image](repo-name.png?raw=true)
	- Finally Click the `Create repository` button<br>
![Image](create-repo-button.png?raw=true)

8. __link(add) your remote GitHub repo to the local one__: Now add your GitHub repo as a remote repo of the local repo you just initialized, using the `remote add` command as follows:
	
```
git remote add origin https://github.com/dbugshe2/sample-repo.git
```	

- the word `origin` is the name we chose to call the remote repo (you can name it anything you want)

- the url that follows is the url of the remote repo, which you can find on the repo page after you have created it (like the screenshot below):<br>
	
![Image](repo-url.png?raw=true)

You can always check what remote repos you have by typing:
	
```
git remote -v
```

9. __Now to Send(Push) Your Project to GitHub__:

Now that you have your empty github repo linked to your local repo, you can send(push) your work to this repo so that it can be seen publicly. 

back to the command line, and enter the `git push` command like below

```
git push -u <remote name> master
```
- replace `<remote name>`with whatever name you chose for your remote repo in step 8
- `master` here simply refers to the default branch on a git repo.

__That's it, if you have been able to complete all the steps, then you have successfully pushed your first git project on to github now go back to your repo (you can find it in your github account page), and you should be able to see your files__
	


## more Information
 below is a list of some of hte best websites and books and videos for learning more about the Python Programming language and Git

### Best Online Resources and Books for Learning about Git

- __Best Online Git Tutorial__: [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials) (Online Tutorial)
- __Best Book to learn Git__ [Pro Git Book](https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf) (PDF)
- __Difference Between Git and GitHub in one Minute__: [What is the difference between Git and GitHub?](https://www.youtube.com/watch?v=xKVlZ3wFVKA) (Youtube)
- __Online Git Tutorial Videos__[Git and Github](https://www.youtube.com/watch?v=vR-y_2zWrIE&list=PLGvfHSgImk4aTlKBUPeC8Eh42LVDcSv9s) (Youtube)


### Best Online Resources and Books for Learning about Python


__work in progress__