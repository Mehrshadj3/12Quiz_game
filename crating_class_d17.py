'''ATRIBUTES'''

class Name0:
    pass

user = Name0()
user.user_id0 = "001"
user.passcode0 = "12345"
print(user.user_id0)
print(user.passcode0)




# pro version




class Name:
    def __init__(self, user_id, passcode):
        self.user_id = user_id
        self.passcode = passcode
        self.followers = 0
        self.following = 0

    '''METHODS'''

    def method_name(self, user1):
        user1.followers += 1
        self.following += 1


user1 = Name("001", "12345")

user1.method_name(user1)

print(user1.user_id)
print(user1.passcode)
print(user1.followers)
print(user1.following)


