class UserManager:

    def __init__(self):
        self._users = []

    def add_user(self, username):
        if not username:
            raise ValueError("Username cannot be empty")
        if username in self._users:
            raise ValueError("User already exists")
        self._users.append(username)

    def remove_user(self, username):
        if username not in self._users:
            raise ValueError("User not found")
        self._users.remove(username)

    def count_users(self):
        return len(self._users)
    
    def count_total_users(self):
        temp = 0
        return len(self._users)