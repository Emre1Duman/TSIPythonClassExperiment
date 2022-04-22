from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Animal"


    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        pass

    def breathe(self):
        pass

    def movement(self):
        pass

    def dies(self):
        pass

    def name(self):
        pass

    def weight(self):
        pass

    def type(self):
        return self.value

class Mammal(Animal):
    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        return "Live Birth" 

    def sleep(self):
        return "I am sleeping now"

    def type(self):
        return self.value

    def breathe(self):
        return "I am breathing"

    def inflight(self):
        flying = False
        return "I am not flying"

class Cat(Mammal):
     #Attributes


    #Constructors
    def __init__(self):
        self.value = "Cat"


    #Methods
    def type(self):
        return self.value

    def name(self):
        return "I am Jerry, a cat"

    def eat(self):
        return "I eat mice"

class Bat(Mammal):
    #Attributes

    #Contructors
    def __init__(self):
        self.value = "Bat"

    def name(self):
        return "I am Batty, a bat"

    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat insects"


class Bird(Animal):
    #attributes

    #constructors
    def __init__(self):
        self.value = "Bird"

    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        return "eggs" 

    def sleep(self):
        return "I am sleeping now"

    def type(self):
        return self.value

    def breathe(self):
        return "I am breathing"

    def inflight(self):
        flying = True
        return "I am flying"

class Penguin(Bird):
    #attributes

    #Constructors
    def __init__(self):
        self.value = "Penguin"

    def name(self):
        return "I am Pengu, a Penguin"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat fish"

    def reproduce(self):
        return "I lay eggs"

class Pigeon(Bird):
    #attributes

    def inflight(self):
        flying = True
        return "I am flying"

    #Constructors
    def __init__(self):
        self.value = "pigeon"

    def movement(self):
        return "I fly"

    def name(self):
        return "I am Pigi, a pigeon"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat worms"

    def reproduce(self):
        return "I build a nest and I lay eggs"

    
    
