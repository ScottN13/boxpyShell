from configparser import ConfigParser
from boxEngine import *
from rich.console import Console

console = Console()
config = ConfigParser(comment_prefixes="#", delimiters="=")


class logins:
    def doLogin():
        OSNAME = os.getlogin()
        bypassLogin = False
        # read how many users exist.
        try:
            config.read("config/users.ini")
            userList = config.sections()
            usercount = 0
            for i in userList: # count how many users.
                usercount += 1
            console.print(f"[bold][bright_green]Number of users found:[/] {usercount} [bright_yellow](including root!)[/]")  
            if usercount == 2:
                console.print(f"[bold]Procceding to login as {OSNAME} (default user)...")
            elif usercount >= 2:
                whichUser = console.input(f"[bold][bright_yellow]Please select which user to login {userList} : ")
                if whichUser == "default":
                    console.print(f"[bold]Procceding to login as {OSNAME} (default user)...")
                elif whichUser != "default" or whichUser != "root":
                    ... # too complicated for my brain

        except Exception as Err:
            console.print_exception(f"[bold][bright_red][Error!] Config file or an element is missing! -> {Err}")

        # permissions check
        try: 
            config.read("config/main.ini")
            login_cnf = str(config["DEBUG"]["skipUsers"])
            if login_cnf == " false":
                bypassLogin = False # will prompt to login as any user besides root.
            elif login_cnf == " true":
                bypassLogin = True # no prompt, login as root if possible.

        except Exception as Err:
            console.print_exception(f"[bold][bright_red][Error!] Config file or an element is missing! -> {Err}")

        
        config.read("config/users.ini")
        tries = 3
        if bypassLogin == False:
            for i in range(0, tries)[::-1]:
                password = str(config["USER"]["pass"])
                passinput = console.input(f"[bold]Please input the password for {OSNAME} :", password=True)
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

        elif bypassLogin == True:
            console.print(f"[[bold][bright_yellow] WARN [/]] skipUsers is set to true! This means you are going to automatically log in as root!")

    def logout():
        ask = console.input(f"[bold][bright_yellow]Are you sure you want to logout?[/] ([bright_green]Y[/]/[bright_red]N[/]): ")
        if ask == "y":
            console.print("[bold][bright_yellow]Ok, logging out...")
            logins.doLogin()
        elif ask == "n":
            print("Ok, did not log out.")

    

