#!/usr/bin/env python3
"""
Interactive Trash Talk Demo - Experience the full power of AI roasting!
"""

import sys
from trash_talk import trash_talk_manager, TrashTalkCategory, IntensityLevel

def interactive_demo():
    print("🔥" * 50)
    print("  WELCOME TO THE TRASH TALK EXPERIENCE!")
    print("🔥" * 50)
    print()
    
    # Enable trash talk
    trash_talk_manager.toggle_trash_talk(True)
    
    # Get opponent name
    opponent = input("Who's your opponent today? (or press Enter for 'Human'): ").strip()
    if not opponent:
        opponent = "Human"
    trash_talk_manager.set_opponent(opponent)
    
    print(f"\n🎯 Locked and loaded for {opponent}!")
    
    while True:
        print("\n" + "="*60)
        print("TRASH TALK MENU:")
        print("1. 🎮 Gaming roasts")
        print("2. 🏃 Sports roasts")
        print("3. 💻 Programming roasts")
        print("4. 🎓 Academic roasts")
        print("5. 👨‍🍳 Cooking roasts")
        print("6. 💬 General roasts")
        print("7. 🌶️ Change intensity")
        print("8. 🎬 Intro roast")
        print("9. 🏆 Victory taunt")
        print("0. 🚪 Exit")
        print("="*60)
        
        choice = input("Choose your weapon: ").strip()
        
        if choice == "0":
            print(f"\n👋 {opponent} got lucky this time! Until next time... 😏")
            break
        elif choice == "1":
            trash_talk_manager.set_category(TrashTalkCategory.GAMING)
            show_category_roasts("GAMING")
        elif choice == "2":
            trash_talk_manager.set_category(TrashTalkCategory.SPORTS)
            show_category_roasts("SPORTS")
        elif choice == "3":
            trash_talk_manager.set_category(TrashTalkCategory.PROGRAMMING)
            show_category_roasts("PROGRAMMING")
        elif choice == "4":
            trash_talk_manager.set_category(TrashTalkCategory.ACADEMIC)
            show_category_roasts("ACADEMIC")
        elif choice == "5":
            trash_talk_manager.set_category(TrashTalkCategory.COOKING)
            show_category_roasts("COOKING")
        elif choice == "6":
            trash_talk_manager.set_category(TrashTalkCategory.GENERAL)
            show_category_roasts("GENERAL")
        elif choice == "7":
            change_intensity()
        elif choice == "8":
            intro = trash_talk_manager.get_trash_talk('intro')
            print(f"\n🎬 INTRO ROAST: {intro}")
            input("\nPress Enter to continue...")
        elif choice == "9":
            victory = trash_talk_manager.get_trash_talk('victory')
            print(f"\n🏆 VICTORY TAUNT: {victory}")
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice! Try again.")

def show_category_roasts(category_name):
    print(f"\n🔥 {category_name} ROASTS - Choose your intensity:")
    print("1. 😊 Mild (friendly banter)")
    print("2. 🌶️ Medium (getting spicy)")
    print("3. 💀 SAVAGE (no mercy)")
    print("4. 🎲 Random intensity")
    print("0. ⬅️ Back to main menu")
    
    while True:
        choice = input("\nIntensity level: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            trash_talk_manager.set_intensity(IntensityLevel.MILD)
            fire_roast("MILD")
        elif choice == "2":
            trash_talk_manager.set_intensity(IntensityLevel.MEDIUM)
            fire_roast("MEDIUM")
        elif choice == "3":
            trash_talk_manager.set_intensity(IntensityLevel.SAVAGE)
            fire_roast("SAVAGE")
        elif choice == "4":
            import random
            intensities = list(IntensityLevel)
            random_intensity = random.choice(intensities)
            trash_talk_manager.set_intensity(random_intensity)
            fire_roast(f"RANDOM ({random_intensity.value.upper()})")
        else:
            print("Invalid choice! Try 1-4 or 0 to go back.")

def fire_roast(intensity_name):
    roast = trash_talk_manager.get_trash_talk()
    print(f"\n🔥💥 {intensity_name} ROAST:")
    print(f"'{roast}'")
    print("\n💀 BOOM! ROASTED! 💀")
    
    again = input("\nWant another one? (y/n): ").strip().lower()
    if again == 'y' or again == 'yes':
        fire_roast(intensity_name)

def change_intensity():
    print("\n🌶️ INTENSITY SETTINGS:")
    print("1. 😊 Mild - Gentle teasing")
    print("2. 🌶️ Medium - Solid burns")
    print("3. 💀 Savage - Nuclear roasts")
    
    choice = input("Set intensity: ").strip()
    if choice == "1":
        trash_talk_manager.set_intensity(IntensityLevel.MILD)
        print("✅ Intensity set to MILD")
    elif choice == "2":
        trash_talk_manager.set_intensity(IntensityLevel.MEDIUM)
        print("✅ Intensity set to MEDIUM")
    elif choice == "3":
        trash_talk_manager.set_intensity(IntensityLevel.SAVAGE)
        print("✅ Intensity set to SAVAGE")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    try:
        interactive_demo()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting... The roasting ends here!")
        sys.exit(0)
