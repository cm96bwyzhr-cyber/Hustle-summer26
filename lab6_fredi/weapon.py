import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        """This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # Use integer division to find half of the max_damage value
        half_damage = self.max_damage // 3

        # Return a random integer between half_damage and max_damage
        return random.randint(half_damage, self.max_damage)
    
if __name__ == "__main__":
    weapon = Weapon("Sword", 50)
    print(weapon.name)
    print(weapon.max_damage)
    print(weapon.attack())
    