class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.following = 0
        self.followers = 0
        self.enemies = []

    def made_an_enemy(self, user):
        self.enemies.append(user)

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(267, "Somba")
user_2 = User(666, "Icen")

user_2.follow(user_1)

print(user_1.followers)
print(user_2.following)
