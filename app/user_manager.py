class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        self.users.append(name)

    def remove_user(self, name):
        self.users.remove(name)

    def count_users(self):
        return len(self.users)
