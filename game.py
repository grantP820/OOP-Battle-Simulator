from goblin import Goblin
from hero import Hero

ARENA_NAME = "cracker barrel"


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
    jimmyAttack = jimmy.attack()
    goblin.take_damage(jimmyAttack)


if __name__ == "__main__":
    main()
