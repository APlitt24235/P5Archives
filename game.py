class Item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect

class Consumable(Item):
    def __init__(self, name, type, effect, quantity):
        super().__init__(name, type, effect)
        self.quantity = quantity

    def use(self, target):
        if self.quantity > 0:
            if self.type == "heal":
                target.hp += self.effect
                if target.hp > target.max_hp:
                    target.hp = target.max_hp
                print(f"{target.name} recovered {self.effect} HP.")
            elif self.type == "sp":
                target.sp += self.effect
                if target.sp > target.max_sp:
                    target.sp = target.max_sp
                print(f"{target.name} recovered {self.effect} SP.")
            self.quantity -= 1
        else:
            print(f"{self.name} is out of stock.")

class Equippable(Item):
    def __init__(self, name, type, effect, equipped):
        super().__init__(name, type, effect)
        self.equipped = equipped

    def equip(self, target):
        if self.equipped:
            print(f"{self.name} is already equipped.")
        else:
            self.equipped = True
            if self.type == "weapon":
                target.strength += self.effect
                print(f"{target.name} equipped {self.name} and increased strength by {self.effect}.")
            elif self.type == "armor":
                target.endurance += self.effect
                print(f"{target.name} equipped {self.name} and increased endurance by {self.effect}.")

class Persona:
    def __init__(self, name, level, hp, sp, strength, magic, endurance, agility, luck, arcana):
        self.name = name
        self.level = level
        self.hp = hp
        self.sp = sp
        self.strength = strength
        self.magic = magic
        self.endurance = endurance
        self.agility = agility
        self.luck = luck
        self.arcana = arcana

    def attack(self, enemy):
        damage = self.strength - enemy.endurance
        enemy.hp -= damage
        print(f"{self.name} dealt {damage} damage to {enemy.name}")

    def cast_spell(self, spell, enemy):
        damage = spell.power + self.magic - enemy.endurance
        enemy.hp -= damage
        self.sp -= spell.cost
        print(f"{self.name} cast {spell.name} and dealt {damage} damage to {enemy.name}")

    def summon(self, player):
        player.persona = self
        print(f"{player.name} has summoned {self.name}")

class Player:
    def __init__(self, name, level, hp, sp, strength, magic, endurance, agility, luck):
        self.name = name
        self.level = level
        self.hp = hp
        self.sp = sp
        self.max_hp = hp
        self.max_sp = sp
        self.strength = strength
        self.magic = magic
        self.endurance = endurance
        self.agility = agility
        self.luck = luck
        self.persona = None

    def attack(self, enemy):
        if self.persona:
            self.persona.attack(enemy)
        else:
            damage = self.strength - enemy.endurance
            enemy.hp -= damage
            print(f"{self.name} dealt {damage} damage to {enemy.name}")

    def cast_spell(self, spell, enemy):
        if self.persona:
            self.persona.cast_spell(spell, enemy)
        else:
            damage = spell.power + self.magic - enemy.endurance
            enemy.hp -= damage
            self.sp -= spell.cost
            print(f"{self.name} cast {spell.name} and dealt {damage} damage to {enemy.name}")

    def summon_persona(self, persona):
        if self.sp >= persona.level * 10:
            persona.summon(self)
        else:
            print("Not enough SP to summon this Persona.")

    def use_item(self, item, target):
        if item in inventory:
            item.use(target)
        else:
            print(f"{item.name} is not in your inventory.")

    def equip_item(self, item):
        if item in self.inventory:
            if isinstance(item, Equippable):
                item.equip(self)
            else:
                print(f"{item.name} cannot be equipped.")
        else:
            print(f"{item.name} is not in your inventory.")

    def pick_up_item(self, item):
        inventory.append(item)
        print(f"{self.name} picked up {item.name}.")

class Enemy:
    def __init__(self, name, level, hp, strength, magic, endurance, agility, luck):
        self.name = name
        self.level = level
        self.hp = hp
        self.strength = strength
        self.magic = magic
        self.endurance = endurance
        self.agility = agility
        self.luck = luck

    def attack(self, player):
        damage = self.strength - player.endurance
        player.hp -= damage
        print(f"{self.name} dealt {damage} damage to {player.name}")

class Spell:
    def __init__(self, name, cost, power):
        self.name = name
        self.cost = cost
        self.power = power

#Adding more functionality to the game
class Map:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

    def enter(self):
        print(f"You have entered {self.name}.")
        while self.enemies:
            enemy = self.enemies.pop(0)
            print(f"You have encountered a {enemy.name}.")
            while enemy.hp > 0 and player.hp > 0:
                #Player turn
                print("Player turn.")
                player_choice = input("what would you like to do? (attack/cast spell/summon persona/use item/equip item)")
                if player_choice == "attack":
                    player.attack(enemy)
                elif player_choice == "cast spell":
                    spell_choice = input("Which spell would you like to cast? (fire/ice)")
                    if spell_choice == "fire":
                        player.cast_spell(fire, enemy)
                    elif spell_choice == "ice":
                        player.cast_spell(ice, enemy)
                elif player_choice == "summon persona":
                    persona_choice = input("Which persona would you like to summon? (arsene/zorro)")
                    if persona_choice == "arsene":
                        player.summon_persona(arsene)
                    elif persona_choice == "zorro":
                        player.summon_persona(zorro)
                elif player_choice == "use item":
                    item_choice = input("Which item would you like to use? (potion/ether)")
                    if item_choice == "potion":
                        player.use_item(potion, player)
                    elif item_choice == "ether":
                        player.use_item(ether, player)
                elif player_choice == "equip item":
                    item_choice = input("Which item would you like to equip? (sword/armor)")
                    if item_choice == "sword":
                        player.equip_item(sword)
                    elif item_choice == "armor":
                        player.equip_item(armor)
                #Enemy turn
                print("Enemy turn.")
                enemy.attack(player)
            #Battle end
            if player.hp > 0:
                print("You have defeated the enemy.")
                #Player obtains loot
                player.pick_up_item(potion)
                player.pick_up_item(ether)
                player.pick_up_item(sword)
                player.pick_up_item(armor)
            else:
                print("You have been defeated.")
                break
        print(f"You have completed {self.name}.")

#Initializing player, personas, and items
player = Player("Joker", 1, 100, 50, 10, 8, 6, 7, 4)

arsene = Persona("Arsene", 1, 75, 20, 8, 10, 6, 7, 5, "Fool")
zorro = Persona("Zorro", 2, 90, 30, 12, 8, 7, 9, 6, "Magician")

potion = Consumable("Potion", "heal", 20, 3)
ether = Consumable("Ether", "sp", 10, 3)

sword = Equippable("Sword", "weapon", 5, False)
armor = Equippable("Armor", "armor", 3, False)

#Initializing spells
fire = Spell("Fire", 10, 15)
ice = Spell("Ice", 12, 18)

#Initializing map and enemies
map1 = Map("Map 1", [Enemy("Shadow", 1, 75, 8, 6, 5, 6, 3), Enemy("Shadow", 2, 90, 10, 8, 6, 7, 4)])
map2 = Map("Map 2", [Enemy("Shadow", 3, 110, 12, 10, 8, 8, 5), Enemy("Shadow", 4, 120, 14, 12, 10, 9, 6)])

#Adding inventory
inventory = []

#Adding a game loop
while player.hp > 0:
    #Display map options
    print("Where would you like to go? (map1/map2) OR would you like to check or use items? (inventory/use)")
    map_choice = input()
    if map_choice == "map1":
        map1.enter()
    elif map_choice == "map2":
        map2.enter()
    #Add option to check inventory
    elif map_choice == "inventory":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for item in inventory:
                print(item.name)
    #Add option to use item
    elif map_choice == "use":
        item_choice = input("Which item would you like to use? ")
        for item in inventory:
            if item.name.lower() == item_choice.lower():
                if item.name == "Potion":
                    player.hp += item.effect
                    print("You have used a potion and regained " + str(item.effect) + " hp.")
                    inventory.remove(item)
                    break
                elif item.name == "Ether":
                    player.mp += item.effect
                    print("You have used an ether and regained " + str(item.effect) + " sp.")
                    inventory.remove(item)
                    break
                else:
                    print("Invalid item.")

#Game over
print("Game Over.")
