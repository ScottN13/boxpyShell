from configparser import ConfigParser 

config = ConfigParser()

config["MAIN"] = {
    "debug" : "false",
    "firstTimeStart" : "false"
    ""
}

config["USER_ADMIN"] = {
    "name" : "Admin",
    "rank" : "sysAdmin",
    "default" : 1,
    "pass" : "123456"
}

config["USER1"] = {
    "name" : "Default User",
    "rank" : "sysUser",
    "default" : 0,
    "pass" : ""
}

with open("mainConfig.ini", "w") as f:
    config.write(f)