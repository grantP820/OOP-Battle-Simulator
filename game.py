from goblin import Goblin
from hero import Hero

ARENA_NAME = "cracker barrel"

def battle(hero: Hero,enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} Wins")
    else:
        print(f"{enemy.name} WIns")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("mushroom")
    newGoblin = Goblin("bigmushroom")
    jimmy = Hero("jimmy")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")
    jimmy=Hero("Jimmy")
    battle(jimmy,goblin)



if __name__ == "__main__":
    main()
