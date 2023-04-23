from pathlib import Path

my_dict = {
"key": "You can used key to open lock. Check if is posible open a door in the office",
"flashlight": "Flashlight, you can use to light the way",
"chair": "Chair is made with wood. It can be helpfull to break something",
"crowbar": "Crowbar is usefull when you have problem with open something, like a door",}

class Space:
    name = f"""You are in an office space. There are many tables and chairs, and
on the tables are computers. You have to find a solution to leave this space.
You have the following options, go to:
- Window
- Door
- Stairs that lead down
Or look around and find something"""
    
    items = ["key", "chair", "crowbar", "flashlight"]
    
    def __init__(self, space_name, position):
        self.space_name = name
        self.position = current_position ##nie wiem czy na 100% potrzebne
        self.items = ["key", "flashlight", "chair", "crowbar"]
        
    def __str__(self):
        return f"{self.space_name}"

class Door(Space):
    door_info = f"""It is only one door in the office. It is look like the door
is the way to outside"""

class Window(Space):
    window_info = f"""In the office are many windows but only one of them can be
your chance to leave"""

class Stairs(Space):
    stairs_info = f"""In the right corner are stairs which follow down."""



class Game:
    inventory = []
    current_posittion = Space
    
    def add_to_inventory(item):
        if len(Game.inventory) < 2:
            Game.inventory.append(item)
            print(f"{item} added to inventory")
        elif len(Game.inventory) > 2:
            print("Inventory is full")

    def check_inventory():
        if Game.inventory == None:
            print("Your backpack is empty")
        else:
            print(f"Backpack: {Game.inventory}")

    # other methods in Game class

    def help():
        print(f"""Instructions:
               help - show help message
               move - move to lacation in office. you have choice between Door,
               Window, Stairs
               take - you take an item which is available in current location
               use -  use item
               check - check your inventory
               look - look arround the office""")

    def move():
        place = input("Where? Window, Stairs, Door? > ").lower()
        if place == "door":
            with open ('Door.txt', 'r', encoding='utf-8') as file1:
                door_see = file1.read()
            Game.current_position = Door
            print(door_see)
        elif place == "window":
            with open ('Window.txt', 'r', encoding='utf-8') as file2:
                window_see = file2.read()
            Game.current_position = Window
            print(window_see)
        elif place == "stairs":
            with open ('Stairs.txt', 'r', encoding='utf-8') as file3:
                stairs_see = file3.read()
            Game.current_position = Stairs
            print(stairs_see)
        else:
            print("You don't have option like this. Is only 3 ways: Door , Window and Stairs")
            return Game.move()

    def look():
        with open ('Look.txt', 'r', encoding='utf-8') as file4:
            look_see = file4.read()
        print(look_see)
        
    @staticmethod
    def take():
        take_item = input("What would you like to put? ").lower()
        if take_item in Space.items:
            return take_item

    def use():
        use_item = input("what would you like to use? ").lower()

        if use_item == "key":
            if use_item not in Game.inventory:
                print(f"You don't have {use_item} in your Backpack")
            elif Game.current_position == Door:
                with open ('Door_use.txt', 'r', encoding='utf-8') as file4:
                    door_use = file4.read()
                print(f"You used {use_item}\n")
                print(door_use,  end="\n\n")
                Game.inventory.remove(use_item)
                new_move = input("What do you do: ").lower()
                if new_move == "move":
                    Game.move()
                elif new_move == "help":
                    Game.help()
                elif new_move == "check":
                    Game.check_inventory()
                elif new_move == "look":
                    Game.look()
                elif new_move == "use":
                    Game.use()
            else:
                print(f"{use_item} can not be used here")
        elif use_item == "chair":
            if use_item not in Game.inventory:
                print(f"You don't have {use_item} in your Backpack")
            elif Game.current_position == Window:
                with open ('Chair_use.txt', 'r', encoding='utf-8') as file5:
                    chair_use = file5.read()
                print(f"You used {use_item}\n")
                print(chair_use, end="\n\n")
                Game.inventory.remove(use_item)
                play_again = input("Would you like to play again? (yes/no) > ").lower()
                if play_again == "y":
                    Game()
                else:
                    print("Thanks for playing!")
            else:
                print(f"{use_item} can not be used here")
        elif use_item == "crowbar":
            if use_item not in Game.inventory:
                print(f"You don't have {use_item} in your Backpack")
            elif Game.current_position == Door:
                with open ('Crowbar_use_door.txt', 'r', encoding='utf-8') as file6:
                    crowbar_use_door = file6.read()
                print(f"You used {use_item}\n")
                print(crowbar_use_door, end="\n\n")
                Game.inventory.remove(use_item)
                play_again = input("Would you like to play again? (yes/no) > ").lower()
                if play_again == "yes":
                    return main()
            elif Game.current_position == Window:
                with open ('Crowbar_use_window.txt', 'r', encoding='utf-8') as file7:
                    crowbar_use_window = file7.read()
                print(f"You used {use_item}\n")
                print(crowbar_use_window, end="\n\n")
                Game.inventory.remove(use_item)
                play_again = input("Would you like to play again? (yes/no) > ").lower()
                if play_again == "yes":
                    return main()
                else:
                    print("Thanks for playing!")
            else:
                print(f"{use_item} can not be used here")
        elif use_item == "flashlight":
            if use_item not in Game.inventory:
                print(f"You don't have {use_item} in your Backpack")
            elif Game.current_position == Stairs:
                with open ('Flashlight_use.txt', 'r', encoding='utf-8') as file8:
                    flashlight_use = file8.read()
                print(f"You used {use_item}\n")
                print(flashlight_use, end="\n\n")
                Game.inventory.remove(use_item)
                print("\nGAME OVER\n")
                return main()
            else:
                print(f"{use_item} can not be used here")


def main():
    game_on = input("Are you ready to begin? please put yes or no. > ").lower()
    if game_on == "yes":
        Game.help()
        print(Space.name)
        while True:
            move_prompt = input("\nWhat do you do: ").lower()
            if move_prompt == "help":
                Game.help()
            elif move_prompt == "move":
                Game.move()
            elif move_prompt == "take":
                item = Game.take()
                while True:
                    if item not in Space.items:
                        print("\nThat item is not here")
                        break
                    elif len(Game.inventory) >= 2:
                        print("\nYour backpack is full")
                        break
                    elif item in Game.inventory:
                        print("\nYou have already picked up that item")
                        break
                    else:
                        Game.inventory.append(item)
                        Space.items.remove(item)
                        print(f"\nYou picked up {item}")
                        print(my_dict[item])
                        break
            elif move_prompt == "use":
                Game.use()
            elif move_prompt == "look":
                Game.look()
            elif move_prompt == "check":
                Game.check_inventory()
            else:
                print("Command is invalid")
    elif game_on == "no":
        print("Ok. thank you")
    else:
        print("Your answer is incorrect. Please try again")
        return main()
    
if __name__ =="__main__":
    main()
