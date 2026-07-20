import random


class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            print(hero.name)
            print("Kills:", hero.kills)
            print("Deaths:", hero.deaths)

    def attack(self, other_team):

        living_heroes = []

        for hero in self.heroes:
            if hero.current_health > 0:
                living_heroes.append(hero)

        living_opponents = []

        for hero in other_team.heroes:
            if hero.current_health > 0:
                living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.battle(opponent)

            living_heroes = []
            for hero in self.heroes:
                if hero.current_health > 0:
                    living_heroes.append(hero)

            living_opponents = []
            for hero in other_team.heroes:
                if hero.current_health > 0:
                    living_opponents.append(hero)

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health