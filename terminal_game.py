# terminal_game.py
import random

print("\n ⊱  ۫ ׅ ✧ INITIATING LINK TO ASTRAL CORE ✶⋆.˚ ")
name = input("Enter your codename: ")
hp = 100
monster_hp = 60
has_key = False
playing = True

print(f"\nWelcome, {name}. You awaken aboard the fractured research station: VIRELUX-7.")
print("The emergency lights flicker. You remember nothing... except a voice: 'Find the Core.'")

while playing:
    print("\nYou are in the Command Hub. What will you do?")
    print("1. Check the broken terminal 📟")
    print("2. Go to the Maintenance Shaft 🔧")
    print("3. Sit and stare into space ⋆⭒˚.⋆🔭")
    print("4. Quit game ❌ ")

    choice = input("> ")

    if choice == "1":
        print("\nThe terminal sparks. A message appears briefly:")
        print(" '...Core breach... unauthorized entity detected... Sector 3 lockdown active.'")
        print("You also find a glowing shard on the floor. It heals you ✙.")
        hp += 10
        if hp > 100:
            hp = 100
        print(f"Your HP is now {hp}. ❤️‍🩹 ")

    elif choice == "2":
        print("\nYou descend into the Maintenance Shaft. It's dark.")
        print("Suddenly, something moves. You see glowing red eyes. It snarls.")

        print("\n!!! BATTLE INITIATED !!!")
        reduced = False
        while monster_hp > 0 and hp > 0:
            print("\nWhat do you do?")
            print("1. Attack")
            print("2. Defend")
            print("3. Hesitate")
            action = input("> ")

            if action == "1":
                print("You slash at the monster!")
                monster_hp -= 20
                print("It shrieks in static and pain! -20 HP to monster.")
            elif action == "2":
                print("You brace for impact. Reduced damage next turn.")
                reduced = True
            else:
                print("You hesitate. The air distorts around you...")
                reduced = False

            if monster_hp > 0:
                damage = random.randint(10, 25)
                if reduced:
                    damage = damage // 2
                hp -= damage
                print(f"The creature lunges! You take {damage} damage!")

        if hp <= 0:
            print("\n✖ You collapse as the creature screeches one last time...")
            print("✖ GAME OVER ✖")
            playing = False

        else:
            print("\n✔ You defeat the monster. Its form melts into data static.")
            print("Among the remains, you find a KEYCARD.")
            has_key = True

    elif choice == "3":
        print("\nYou sit in silence. The stars outside pulse. You feel a strange calm.")
        print("You regain 5 HP.")
        hp += 5
        if hp > 100:
            hp = 100

    elif choice == "4":
        print("\n✦ LINK TERMINATED. GOODBYE, INTERLOPER. ✦")
        playing = False

    else:
        print("\nYou hesitate. Nothing happens.")

    if playing and hp > 0:
        print(f"\nYour current HP is: {hp}")
        print("\nDo you want to proceed to the Core Chamber? (yes/no)")
        next_step = input("> ")

        if next_step.lower() == "yes":
            print("\nYou approach the Core Chamber.")
            if has_key:
                print("The keycard activates the door. Inside is a glowing fractured star.")
                print("A panel lights up. Choose:")
                print("1. Stabilize the Core 🌌 ")
                print("2. Absorb its power 🐦‍🔥")
                print("3. Destroy it 💥 ")

                final_choice = input("> ")

                if final_choice == "1":
                    print("\nYou stabilize the Core. Light returns to the station.")
                    print("🟢 Ending: The Guardian of Light")
                elif final_choice == "2":
                    print("\nYou absorb the Core. Power floods you. The station burns.")
                    print("🔴 Ending: The Vessel of the Void")
                elif final_choice == "3":
                    print("\nYou destroy the Core. A blinding light ends everything.")
                    print("⚪ Ending: The Final Silence")
                else:
                    print("\nThe panel glitches. Reality fractures.")
                    print("❓ Ending: Unknown Fate")
                playing = False
            else:
                print("The Core Chamber is locked. You need a keycard.")
        else:
            print(f"\n{name} returns to the Command Hub, uncertain but alive.")
            print("✧ Adventure paused ✧")
            playing = False

