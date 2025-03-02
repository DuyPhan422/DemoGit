import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.hp -= damage
        print(f"{self.name} tấn công {other.name} gây {damage} sát thương!")

    def is_alive(self):
        return self.hp > 0

class Hero(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)

    def special_attack(self, other):
        damage = random.randint(self.attack_power, self.attack_power * 2)
        other.hp -= damage
        print(f"{self.name} sử dụng chiêu đặc biệt tấn công {other.name} gây {damage} sát thương!")

class Enemy(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)

    def taunt(self):
        print(f"{self.name} nói: 'Người sẽ không bao giờ đánh bại ta!'")

    def special_attack(self, other):
        damage = random.randint(self.attack_power, int(self.attack_power * 1.5))
        other.hp -= damage
        print(f"{self.name} sử dụng chiêu đặc biệt tấn công {other.name} gây {damage} sát thương!")

def battle(hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        if random.choice([True, False]):
            hero.special_attack(enemy)
        else:
            hero.attack(enemy)
        
        if not enemy.is_alive():
            print(f"{hero.name} đã chiến thắng!")
            break

        enemy.taunt()
        enemy.special_attack(hero)

        if not hero.is_alive():
            print(f"{enemy.name} đã chiến thắng!")
            break

        print(f"Lượng máu: {hero.name}: {hero.hp} HP | {enemy.name}: {enemy.hp} HP\n")

hero = Hero("Chiến Binh", 100, 20)
enemy = Enemy("Quái Vật", 100, 20)

battle(hero, enemy)
