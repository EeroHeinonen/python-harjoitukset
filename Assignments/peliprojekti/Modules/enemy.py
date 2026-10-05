#Used to clear the console using system("cls")
from os import system
#Import Money class from sibling module
from .item import Money
import random
#Initiate class "Enemy"
class Enemy:
    def __init__(self, name, health, damage, currentRoom, itemHeld):
        self.name = name
        self.health = health
        self.damage = damage
        self.currentRoom = currentRoom
        self.itemHeld = itemHeld

    #Method to handle enemy attacks, with a 1 in 3 chance for the attack to hit
    def attack(self, target):
        hitChance = random.randint(1,3)
        if hitChance == 3:
            #Subtract the enemy's damage from the player's health
            target.health -= self.damage
            print(f"The enemy damaged you for {self.damage}!")
        #Inform the player if the enemy missed
        else:
            print(f"The enemy attempted to damage you but missed!")

    #Method to handle the player damaging the enemy
    def takeDmg(self, playerItem):
        #Subtract the damage of the item the player used, from enemy's health
        self.health -= playerItem.dmg
        system("cls")
        print("Item used!")
        #Check if enemy health is above zero
        if self.health > 0:
            print(f"You did {playerItem.dmg} damage and the enemy's health was lowered to {self.health}!")
            input("Press any key to continue...")
        #Inform the player that they have defeated the enemy and delete the enemy from the room's "enemies" list
        else:
            print("You have defeated the enemy!")
            #"Drop" the item held to the room's "items" list if it is not money in the amount of 0 aka. empty
            if issubclass(type(self.itemHeld), Money) and self.itemHeld.amount <= 0:
                print("The enemy dropped nothing!")
            else:
                if issubclass(type(self.itemHeld), Money):
                    print(f"The enemy dropped money in the amount of {self.itemHeld.amount}!")
                    self.currentRoom.items.append(self.itemHeld)
                else:
                    print(f"The enemy dropped a / an {self.itemHeld.name}!")
                    self.currentRoom.items.append(self.itemHeld)
            self.health = 0
            self.currentRoom.enemies.remove(self)
            input("Press any key to continue...")