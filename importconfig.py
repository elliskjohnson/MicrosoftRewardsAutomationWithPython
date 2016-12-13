import configparser
from Users import User


def get_config():
    cfg = configparser.ConfigParser()
    cfg.read("config.cfg")
    keys = []

    for string in str(cfg.get("DEFAULT","keys")).strip().split(","):
        keys.append(string.strip())

    list_users =[]

    for value in keys:
        newUser = User(value, cfg.get(value, "Username"), cfg.get(value, "Password"), cfg.get(value, "RewardLevel"))
        list_users.append(newUser)

    return list_users

# Unit test
if __name__ == "__main__":
    for val in get_config():
        print(val)
