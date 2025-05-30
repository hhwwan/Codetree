user2_id, user2_level = input().split()
user2_level = int(user2_level)

class user:
    def __init__(self, user_id='codetree', user_level=10):
        self.i_d = user_id
        self.level = user_level

user1 = user()
print('user', user1.i_d, 'lv', user1.level)

user2 = user(user2_id,user2_level)
print('user', user2.i_d, 'lv', user2.level)