class Wizard:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def player(self, user_effect):
        return user_effect * 8

user1 = Wizard('ALi',31,'black')

result = user1.player(12)
print(f"{user1.age} {user1.color} from {user1.name}")

print(result)

