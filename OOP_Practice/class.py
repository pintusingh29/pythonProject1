class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers_count = 0

user_1 = User("001", "angela")