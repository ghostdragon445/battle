from classes.game import Person, bcolours
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 20, 200, "white")

# Create Items
potion = Item("Potion", "potion", "heals 50hp", 50)
hipotion = Item("Hi-Potion", "potion", "heals 100hp", 100)
superpotion = Item("Super Potion", "potion", "heals 500hp", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one group member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP of the party", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5}, {"item": hielixer, "quantity": 5},
                {"item": grenade, "quantity": 3}]

# Instantiate people (name, hp, mp, atk, df, magic, items)
player1 = Person("Valos:", 3260, 132, 132, 34, player_spells, player_items)
player2 = Person("Ben  :", 4160, 188, 188, 34, player_spells, player_items)
player3 = Person("Bob  :", 3089, 174, 174, 34, player_spells, player_items)

enemy1 = Person("Imp :", 1250, 130, 560, 325, [], [])
enemy2 = Person("Mangus:", 11200, 65, 221, 25, [], [])
enemy3 = Person("Imp :", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
w = 1

print(bcolours.FAIL + bcolours.BOLD + "AN ENEMY ATTACKS!" + bcolours.ENDC)

while running:
    print("==================================")

    print("\n\n")
    print("NAME:                 HP:                                                  MP:")
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            player.choose_target(enemies)
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) -1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolours.FAIL + "\nNot enough MP\n" + "\n Current MP:" + str(player.get_mp()) + bcolours.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolours.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP:" + bcolours.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolours.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage!" + bcolours.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolours.FAIL, "You don't have any of this item left" + bcolours.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolours.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP:", bcolours.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolours.OKGREEN + "\n" + item.name + " fully restored HP/MP" + bcolours.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolours.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage" + bcolours.ENDC)

    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemy.generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg,)

    if enemy.get_hp() == 0:
        print(bcolours.OKGREEN + "You win" + bcolours.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolours.FAIL + "You have been defeated." + bcolours.ENDC)
        running = False