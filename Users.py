class User:
    __slots__ = "_key", "_username", "_password", "_level", "_num_times"

    def __init__(self, key, username, password, level):
        self._key = str(key)
        self._username = str(username)
        self._password = str(password)
        self._level = int(level)

    def __str__(self):
        return str(self._key + " " + self._username + " " + self._password + " " + self._level)

    def get_key(self):
        return str(self._key)

    def get_username(self):
        return str(self._username)

    def get_pw(self):
        return str(self._username)

    def get_lvl(self):
        return int(self._level)

    def get_num_times(self):
        if self._level == 1:
            return int('10')
        elif self._level == 2:
            return int('30')
