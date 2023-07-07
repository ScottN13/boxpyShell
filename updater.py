from boxEngine import warn, error, success
import git
import shutil
from configparser import ConfigParser
from rich.console import Console
from os import system, name

console = Console()
clear = lambda: system("cls" if name == "nt" else "clear")

class updater:
    def __init__(self):
        self.config = ConfigParser(comment_prefixes="#", delimiters="=")
        self.config.read("config/main.ini")
        self.current_version = str(config["MAIN"]["version"])  # Gets version from config main.ini
        self.current_channel = str(config["MAIN"]["channel"])  # Gets branch selection from config main.ini
        
    # Automatically pulls from 
    def update(self):
        self.branch = self.current_channel
        if self.branch == "main":
            # Replace these with your own values
            self.repo_url = "https://github.com/ValkTheBoxman/boxpyShell"
            self.local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            self.repo = git.Repo.clone_from(self.repo_url, self.local_path, branch='main')

            # Replace the old code with the new code
            shutil.rmtree("/path/to/old/folder")
            shutil.move(self.local_path, "/path/to/old/folder")

        elif branch == "dev":
            # Replace these with your own values
            self.repo_url = "https://github.com/ValkTheBoxman/boxpyShell/tree/dev"
            self.local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            self.repo = git.Repo.clone_from(self.repo_url, self.local_path, branch='dev')

            # Replace the old code with the new code
            shutil.rmtree("/path/to/old/folder")
            shutil.move(self.local_path, "/path/to/old/folder")

    def check(self):
        self.branch = self.current_channel
        if self.branch == "main":
            self.repo_url = "https://github.com/ValkTheBoxman/boxpyShell/"
            self.local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            self.repo = git.Repo.clone_from(repo_url, local_path, branch='main')

            # Check the latest version of the code on GitHub
            self.latest_version = repo.git.describe('--tags', '--abbrev=0')

            # Replace the old code with the new code if the latest version is different
            if self.latest_version != self.current_version:
                warn(f"A new update ({self.latest_version}) is available! Use the updater to update to the latest version.")
            else:
                success("You have the latest version of the code!")

        elif self.branch == "dev":
            self.repo_url = "https://github.com/ValkTheBoxman/boxpyShell/tree/dev"
            self.local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            self.repo = git.Repo.clone_from(repo_url, local_path, branch='main')

            # Check the latest version of the code on GitHub
            self.latest_version = repo.git.describe('--tags', '--abbrev=0')

            # Replace the old code with the new code if the latest version is different
            if self.latest_version != self.current_version:
                warn(f"A new update ({self.latest_version}) is available! Use the updater to update to the latest version.")
            else:
                success("You have the latest version of the code!")


while True:
    console.print("[bold]Welcome to the boxpyshell updater![/]")
    updater.check()
    
    user_input = console.input("[bold]Type [yellow]'Help'[/] to see all the available options.\n -> [/]").title()

    if user_input in ("Help", "H"):
        console.print("Update Command -> Checks for update and installs it if an update is available.\nDownload Command -> It does something I guess\nExit Command -> Exits program.")

    if user_input in ("Exit", "E"):
        exit(0)

    elif user_input in ("Update", "U"):
        warn("Are you sure you want to update? Please make sure that boxpyshell is closed before continuing.")
        confirm = console.input("[bold]Confirm? ([bright_green]Y[/]/[bright_red]N[/]) -> [/]")
    
    elif user_input in ("Download", "D"):
        warn()
