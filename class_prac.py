class Presenter():
    def __init__(self, name, age):
        #constructor
        self.name = name #property
        self.age = age
    
    @property
    def name(self):
        print('in the getter')
        return self.__name
    
    @name.setter
    def name(self, value):
        print('In the setter')
        #cool validation here
        self.__name = value

    @property
    def age(self):
        print('age getter')
        return self.__age
    @age.setter
    def age(self, value):
        print('age setter')
        self.__age = value

    def say_hello(self):
        print(self.name, 'and age is', self.age)
    
presenter = Presenter('Chris', 10)
presenter.name = 'Christopher'
presenter.age = 100
presenter.say_hello()