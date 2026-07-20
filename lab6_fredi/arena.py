from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:

    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")


    def create_ability(self):

        name = input("magic")
        max_damage = int(input("39"))

        return Ability(name, max_damage)


    def create_weapon(self):

        name = input("What is the weapon name? ")
        max_damage = int(input("19"))

        return Weapon(name, max_damage)


    def create_armor(self):

        name = input("shield")
        max_block = int(input("17"))

        return Armor(name, max_block)


    def create_hero(self):

        hero_name = input("Hero's name: ")

        hero = Hero(hero_name)

        add_item = ""

        while add_item != "4":

            add_item = input(
                "[1] Add ability\n"
                "[2] Add weapon\n"
                "[3] Add armor\n"
                "[4] Done adding items\n"
                "Your choice: "
            )


            if add_item == "1":

                ability = self.create_ability()
                hero.add_ability(ability)


            elif add_item == "2":

                weapon = self.create_weapon()
                hero.add_weapon(weapon)


            elif add_item == "3":

                armor = self.create_armor()
                hero.add_armor(armor)


        return hero


    def build_team_one(self):

        number = int(input("5"))

        for i in range(number):

            hero = self.create_hero()

            self.team_one.add_hero(hero)



    def build_team_two(self):

        number = int(input("5"))

        for i in range(number):

            hero = self.create_hero()

            self.team_two.add_hero(hero)



    def team_battle(self):

        self.team_one.attack(self.team_two)



    def show_stats(self):

        print("\n")
        print(self.team_one.name + " statistics:")
        self.team_one.stats()

        print("\n")
        print(self.team_two.name + " statistics:")
        self.team_two.stats()


        team_one_alive = 0
        team_two_alive = 0


        for hero in self.team_one.heroes:
            if hero.current_health > 0:
                team_one_alive += 1


        for hero in self.team_two.heroes:
            if hero.current_health > 0:
                team_two_alive += 1


        if team_one_alive > team_two_alive:
            print(self.team_one.name + " wins!")

        elif team_two_alive > team_one_alive:
            print(self.team_two.name + " wins!")

        else:
            print("Draw")



if __name__ == "__main__":

    game = Arena()

    game.build_team_one()
    game.build_team_two()

    playing = True

    while playing:

        game.team_battle()

        game.show_stats()

        again = input("Play Again? Y or N: ")

        if again.lower() == "n":
            playing = False

        else:
            game.team_one.revive_heroes()
            game.team_two.revive_heroes()