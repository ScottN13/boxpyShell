from configparser import ConfigParser
from extShellData import *
from rich.console import Console

console = Console()
config = ConfigParser()
passPrint = "Please input password (Press enter if none was added): "

# permissions check
try: 
    config.read("config/main.ini")
    login_cnf = str(config["DEBUG"]["skipUsers"])
    if login_cnf == "true":
        bypassLogin = False # will prompt to login as any user besides root.
        config.read("config/users.ini")
    elif login_cnf == "false":
        bypassLogin = True # no prompt, login as root.

except Exception as Err:
    console.print_exception(f"[bold][bright_red][Error!] Config file or an element is missing! -> {Err}")


class logins:
    def doLogin():
        config.read("config/users.ini")
        tries = 3
        OSNAME = os.getlogin()
        for i in range(0, tries)[::-1]:
            password = str(config["USER"]["pass"])
            passinput = console.input(f"[bold]Please input the password for {OSNAME} :")
            if passinput == password:
                console.print(f"[bold][bright_green]Success! Logged in as {OSNAME}!")
                break

            elif passinput != password:
                tries -= 1
                console.print(f"[bold][bright_red]Error! Wrong password!, {tries} tries remaning.")
                if tries <= 0:
                    console.print("[bold][bright_red]Password typed in wrong too many times. Re-run the program to try again.")
                    sys.exit()
                continue

    def logout():
        ask = console.input(f"[bold][bright_yellow]Are you sure you want to logout?[/] ([bright_green]Y[/]/[bright_red]N[/]): ")
        if ask == "y":
            console.print("[bold][bright_yellow]Ok, logging out...")
            logins.doLogin()
        elif ask == "n":
            print("Ok, did not log out.")


