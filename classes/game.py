import random

class bcolours:
    HEADDER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        act = 1
        print("\n" + bcolours.OKGREEN + bcolours.BOLD + "ACTIONS" + bcolours.ENDC)
        for item in self.actions:
            print(str(act) + ":", item)
            act += 1

    def choose_magic(self):
        mact = 1
        print("\n" + bcolours.OKGREEN + bcolours.BOLD + "MAGIC:" + bcolours.ENDC)
        for spell in self.magic:
            print(str(mact) + ":", spell.name, "(cost:", str(spell.cost) + "}")
            mact += 1

    def choose_item(self):
        iact = 1

        print("\n" + bcolours.OKGREEN + bcolours.BOLD + "ITEMS:" + bcolours.ENDC)
        for item in self.items:
            print("  " + str(iact) + ".", item["item"].name + ":", item["item"].description, "(x" + str(item["quantity"] + ")"))
            iact += 1
