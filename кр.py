# 1
class BasePerson:
    def __init__(self, uid, name):
        self.id = uid
        self.name = name

    def __repr__(self):
        return 'name: {a}, id: {b}'.format(a=self.name, b=self.id)

class Person(BasePerson):
    def __init__(self):


print(BasePerson(2020, 'oleg'))
