from configparser import ConfigParser
from extShellData import *
from boxpyshell import cmdTagSuffix
from boxpyshell import cmdTagPrefix

config = ConfigParser()
config.read("mainConfig.ini")
passPrint = "Please input password (Press enter if none was added): "
bypassLogin = False
cmdTagPrefix = "@boxpyshell $~: "
cmdTagSuffix = ""

class logonSession:
    def doLogin():
        try:
            ConfigDebugCheck = str(config["MAIN"]["skipUsers"])
            if ConfigDebugCheck == "false":
                if bypassLogin == False:
                    user = input("Please login (Admin or User1): ")
                    bypassLogin == True

                if user == "USER1":
                    cmdTagSuffix += "default"
                    cmdTagFull = str(cmdTagSuffix + cmdTagPrefix)

                if user == "ADMIN":
                    password = input(passPrint)
                    cmdTagSuffix += "sysAdmin"
                    cmdTagFull = str(cmdTagSuffix + cmdTagPrefix)
                    if password != "123456":
                        print("Wrong Password! Exiting...")
                        exit(0)

                    try:
                        config_data2 = config[user]
                    
                    except:
                        print("User Not found! Exiting...")
                        exit(0)


            elif ConfigDebugCheck == "true":
                print("skipping user selection")
                cmdTagSuffix += "debug"
                cmdTagFull = str(cmdTagSuffix + cmdTagPrefix)

        except:
            exit("Error! Config file or an element is missing!")



        try:
            config_data1 = str(config["MAIN"]["debug"])
            if config_data1 == "false":
                animlib.loadingAnim("load",5)
            elif config_data1 == "true":
                print("debug mode = true")
                debugMode = True

        except:
            exit("Error! Config file or an element is missing!")

"""
        elif command == "debug":
        if debugMode == True:
            print("entered debug mode")
            print("please wait, retrieving data....")

            try:
                debugChk = config['DEBUG']
                print('Here is a list of the debugging configs:')
                print(debugChk)
                debugApplyAsk = input("Would you like to apply these changes next startup? (Y/N)")
                if debugApplyAsk == "y" or debugApplyAsk == "Y":
                    print("Writing changes..")
                    

            except:
                print("User Not found! Exiting...")
                exit(0)

"""