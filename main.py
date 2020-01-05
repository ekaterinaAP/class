class Animal:
    #state = "hungry"
    #voice = "silent"
    total_weight = 0
    ferma = {}
    
    def __init__ (self, name = "животина", weight = 0):
        self.name = name
        self.weight = weight
        Animal.total_weight += weight
        #Animal.ferma.append(self.weight)
        Animal.ferma[self.weight]=self.name

      
    def feed(self):
        self.state = "fed"
        print(f"{self.name} теперь накормлен")

    def get_hungry(self,hour):
        if hour > 4:
            self.state = "hungry again"
        else:
            self.state = "fed"
            
    def talk(self):
        print("Все разговаривают по-разному")
        self.voice = "loud"   
         
class Milk(Animal):
    #udder = "full"

    def milking(self):
        self.udder = "empty" 
        print(f"{self.name} подоена")

class Egg(Animal):
    #egg = "it's time to collect"

    def collection(self):
        self.egg = "eggs collected"
        print(f"у {self.name} яйца собраны")

class Goose(Egg, Animal):
    voise = "ga-ga-ga"

class Cow(Milk, Animal):
    voise = "mu"

class Sheep(Animal):
    wool = "long"
    voise = "be-e-e"
    
    def shear(self):
        self.wool = "short"
        print(f"{self.name} пострижен")
 
class Сhicken(Egg, Animal):
    voise = "ko-ko-ko"

class Goat(Milk, Animal):
    voise = "me-e-e"

class Duck(Egg, Animal):
    voise = "krya"


goose0 = Goose("Серый",5)
goose1 = Goose("Белый",4)
cow0 = Cow("Манька",300)
sheep0 = Sheep("Барашек",50)
sheep1 = Sheep("Кудрявый",53)
chicken0 = Сhicken("Ко-ко",2)
chicken1 = Сhicken("Кукареку",2.5)
goat0 = Goat("Рога",52)
goat1 = Goat("Копыта",51)
duck0 = Duck("Кряква",4)

goose0.feed()
goose1.feed()
cow0.feed()
sheep0.feed()
sheep1.feed()
chicken0.feed()
chicken1.feed()
goat0.feed()
goat1.feed()
duck0.feed()

print()
goose0.collection()
goose1.collection()
duck0.collection()
chicken0.collection()
chicken1.collection()

print()
sheep0.shear()
sheep1.shear()

print()
goose0.talk()
print(f"например,{goose0.name} говорит {goose0.voise}")

print()
print(f"Общий вес всех животных: {Animal.total_weight}")

#print()
#print(Animal.ferma)
#Animal.ferma.sort()
#print(Animal.ferma[-1])

print()
print(f"самое тяжёлое животное на ферме весит {max(Animal.ferma)} кг, его зовут {Animal.ferma[max(Animal.ferma)]}")