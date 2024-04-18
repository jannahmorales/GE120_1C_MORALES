# OBJECT ORIENTED PROGRAMMING

#Creating Classes
class Crayon: #standard to capitalize
    pass

redCrayon = Crayon() #class instantation

print(type(redCrayon))

# creating ML HEROES
class MLHero:
    def __init__(self, name, description="Twilight Goddess"):
        self.name = name
        self.description = description
        role = "Mage"
        self.role = role.upper()[0]
        self.specialty = "Damage/Poke"
        self.statistics = {
            "durability": 60,
            "offense": 80,
            "skill_effects": 50,
            "difficulty": 70
        }
    def skill(self):
        print(self.name + "used the ATTACK")
    def superSkill(self, opponent):
        print(self.name + "used SUPERKILL against" + opponent)
hero = MLHero("Lunox", "MasipagNaUPStudent")
print("Hero Name:", hero.name)
print("Hero Desc:", hero.description)
print("Hero ROle:", hero.role)
print("Hero Specialty:", hero.specialty.split("/"))
print("Hero Offense+Difficulty:", hero.stastics["offense"] + hero.stastics["difficulty"])

hero.superSkill("Zilong")