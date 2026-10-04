#Initiate class "Enemy"
class Enemy:
    def __init__(self, name, health, damage, currentRoom):
        self.name = name
        self.health = health
        self.damage = damage
        self.currentRoom = currentRoom