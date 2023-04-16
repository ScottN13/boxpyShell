from boxEngine import warn,error,success
import git
import shutil
from configparser import ConfigParser
from rich.console import Console

console = Console()
config = ConfigParser(comment_prefixes="#", delimiters="=")
config.read("config/main.ini")
current_version = str(config["MAIN"]["version"])  # Gets version from config main.ini
current_channel = str(config["MAIN"]["channel"])  # Gets branch selection from config main.ini

class updater:
    # Automatically pulls from 
    def update():
        branch = current_channel
        if branch == "main":
            # Replace these with your own values
            repo_url = "https://github.com/ValkTheBoxman/boxpyShell"
            local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            repo = git.Repo.clone_from(repo_url, local_path, branch='main')

            # Replace the old code with the new code
            shutil.rmtree("/path/to/old/folder")
            shutil.move(local_path, "/path/to/old/folder")

        elif branch == "dev":
            # Replace these with your own values
            repo_url = "https://github.com/ValkTheBoxman/boxpyShell/tree/dev"
            local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            repo = git.Repo.clone_from(repo_url, local_path, branch='dev')

            # Replace the old code with the new code
            shutil.rmtree("/path/to/old/folder")
            shutil.move(local_path, "/path/to/old/folder")

    def check():
        branch = current_channel
        if branch == "main":
            repo_url = "https://github.com/ValkTheBoxman/boxpyShell/"
            local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            repo = git.Repo.clone_from(repo_url, local_path, branch='main')

            # Check the latest version of the code on GitHub
            latest_version = repo.git.describe('--tags', '--abbrev=0')

            # Replace the old code with the new code if the latest version is different
            if latest_version != current_version:
                warn(f"A new update ({latest_version}) is available! Use the updater to update to the latest version.")
            else:
                success("You have the latest version of the code!")

        elif branch == "dev":
            repo_url = "https://github.com/ValkTheBoxman/boxpyShell/tree/dev"
            local_path = "/path/to/local/folder"

            # Clone the latest code from the GitHub repository
            repo = git.Repo.clone_from(repo_url, local_path, branch='main')

            # Check the latest version of the code on GitHub
            latest_version = repo.git.describe('--tags', '--abbrev=0')

            # Replace the old code with the new code if the latest version is different
            if latest_version != current_version:
                warn(f"A new update ({latest_version}) is available! Use the updater to update to the latest version.")
            else:
                success("You have the latest version of the code!")


while True:
    console.print("[bold]Welcome to the boxpyshell updater!")
    updater.check()
    uInput = input("user: ")

    if uInput == ["exit","e","Exit"]:
        exit(0)

    elif uInput == ["update","u"]:
        warn("Are you sure you want to update? Please make sure that boxpyshell is closed before continuing.")
        confirm = console.input("Confirm? ([bright_green]Y[/]/[bright_red]N[/]) :")
    
    elif uInput == "download" or uInput == "d":
        warn()
