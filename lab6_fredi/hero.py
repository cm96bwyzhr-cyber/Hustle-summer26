import random
from ability import Ability
from armor import Armor
from weapon import Weapon
class Hero:
    def __init__(self, name, starting_health=100): # starting health=100 makes the starting health orgument OPTIONAL
         self.name = name
         self.starting_health = starting_health
         self.current_health = starting_health
         self.abilities = []
         self.armor = []
         self.kills = []
         self.deaths = []
         
    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        print(random.choice(my_list))

    def add_ability(self, ability): # adds an ability to a hero's list of abilities
       self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        print (total_damage) 
        return total_damage
    
    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        total_block = 0 
        for armor in self.armors:
            total_block += armor.block
        print(total_block)
        return total_block
    
    def take_damage(self, damage):
        blocked = self.defend()
        actual_damage = max(damage - blocked, 0)
        self.current_health -= actual_damage
        if self.current_health < 0:
            self.current_health = 0
        print(self.current_health)
        return actual_damage

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_ability(self, ability): # adds an ability to a hero's list of abilities
       self.abilities.append(ability)

    def add_weapon(self, weapon):
       self.abilities.append(weapon)

    def attack(self):
        total_damage = 10
        for ability in self.abilities:
            total_damage += ability.attack()
        print(total_damage)
        return total_damage

if __name__ == "_main_": 
   my_hero = Hero ("Spider-Man", 150) # 150 is our starting health
   #print(my_hero.name)
   #print(my_hero.current_health)
   #my_opponent = hHero("super_man", 1000)
   #my_hero. battle(my_opponent)
   #my_hero.add_ability(Ability("Web Shooter", 25))
   #my_hero.add_ability(Ability("spidey senses", 10))
   #my_hero.attack()
   my_hero.add_armor(Armor("hat", 10))
   my_hero.add_armor(Armor("chest_plate", 20))
   my_hero.add_armor(Armor("gun", 13))
   # my_hero.defend()
   my_hero.take_damage(40)
