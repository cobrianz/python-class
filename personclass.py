class Person:
    def __call__(self, name):
        self.name = name
    def talk(self):
        print ("talk")

john = Person("John Doe")
print(john.name)
john.talk()