

Zombie = "You've encountered a Zombie"
print(Zombie)

Zombie_attack = "Zombie attacks!"
health = "100"
zombie_health = "Zombie has 100hp."
dead = "0"
print(zombie_health)
while health > dead:
    health = input(int("Current mob Health."))
    if health == dead:
        print("Zombie has perished.")
    else:
        print(Zombie_attack)

press_enter = input("Press enter to continue.")
print(press_enter)
print("Party continues walking through door.")
