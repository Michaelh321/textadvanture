print(
    "It is a Halloween night. You the player and your 4 friends have been going house to house and geeting candy. You guys are those kids. Those kids that mess up people lawns by stepping on them. You guys reach this one house at the end of the block. The house looks very scary, but you and your friend still walk up to it. When you are about to knock on the door, You hear a loud murding screem coming from the house. You look at your friends and now you guys are laughing. Then you hear somebody trying to open the door. You can tell that theyre are many locks. The sound of the mystery person tring their all to open the door scard the *!%@ out of you guys. You guys book it into the trees next to the house. As you guys hide next to the trees you see a old ragdy woman on the door steeps of the porch. You guys think its some old grandma. One of your friends coughs and she looks towards your direnction. You guys starting running with all your will into the forest. You and your friends are running on a path towards the unknown. . .  ")

print("")
print("")
print("")
print("")

answer = input("Would You like to Play My Game? (yes/no) ")

if answer.lower().strip() == "yes":
    answer = input("You and your 4 friends reach and abandoned building. Do You choose to go in?(yes/no) ").lower().strip()

    if answer == "yes":
        answer = input("You and Your tired friends walk into the Abandon Building.You get an option, go left or right ")

        if answer == "left":
            print("You go left")
            answer = input ("You see a long hall way. You and your friends walk down it. As You reach the end, its a dead end. But you see a sword on the ground. Do you want to pick it up?(yes/no)  ")
            if answer == "yes":
                answer = input("You have picked up a rusty sword. It is kinda heavy. You show it to your friends. As you let you friends see it you see a monster in the behind your friends do you wish do attack it.(yes/no) ")
                if answer == "yes":
                    print("You tell your friends to watch out as you run towards the monster with the sword. You shove the sword threw the monsters chest killing it. ")
                    answer = input ("Do you want to leave the building (yes/no) ")
                    if answer == "yes":
                        print("As you look down at the monster you are so confused on whats going on in this building. You and your frinds get the smart idea to reach the entrance and leave the building. You guys walk towards the entrance. Once you guys reach it you see that grandma that was chasing you and your friends. You walk up to her and start to notice that she is not a regular grandma. She has eyes that are completely blacked out and she is floating above the ground. You and your friends come to the conclusin that she is a demon. You pick up the sword and throw it at her. with one nice throw it reaches her and penetrates through her shoulder she drops to the ground and you guys start running. back to the roads. You guys reach the roads and you guys are out of breath. You and your friends say good bye to each other and go home. As you are walking home alone your start to hear a ringing sound coming from the sky. You look up and see a red thing in the sky. You can barely see it. You do not know what it is. Then you hear a loud screeching sound. You look back to down an see a car heading righ for you. The car is coming way too quick and you cannot move out in time. You close your eyes and then nothing happens. You open then quickly and you are in your bed. You just woke up from a dream. Everything that just happened was not real. You have won the game.  ")
                    elif answer == "no":
                        print("You and your friends are too wild up. You guys want to explorer more. As you guys start heading back you see the grandma. You run up to her and you notice that she is not a regular grandma. She has eyes that are completely blacked out and she is floating above the ground. You are kinda freaked out by this and head back. As you and your guys reach the dead end You turn around. You see the grandma floating and want to attack her. As you try to swing your sword she pick you up with her hands. Then she throws you against the wall. You black out. Time passes and then you wake up. All you see is white. You are in Heaven. You lost the game. Restart.  ")
                elif answer == "no":
                    print("You are too scared to attack it. You run in the opposite direction. You remember that it is a dead end. You then turn around and see your friends running towards you as the monster is running after them. You are still in your tracks. You are too scared too move. Then the monster reaches you and eats you guys whole. You have lost the game. ")
            elif answer == "no":
                print("You do not pick up the sword. You and your friends now walk back in the direction you came from. Then you see a monster. The monster attacks you and then you guys die. You lost the game. Try again.")

        elif answer == "right":
            print("You go right")
            answer = input("You see a monster. Do you choose to attack or run. ")
            if answer == "attack":
                print("You and your frineds attack the monster with your bare hands. As you guys are hitting the monster he opnes his mouth and eats you one by one whole. You have lost the game. Try again.")

            elif answer == "run":
                print("You and your friends start booking it to the entrance. One of your friends trips and you look back. You see the monster opens his mouth and swallows your friend whole. You then turn back around. You reach the entrance and you see the old looking grandma. You are petrified. she walks up to you and your friends. Then with one scope, the granny picks you up with no problem and throws you across the woods. You hit the trees and black out. Time passes and then you wake up. All you see is white. You are in Heaven. You lost the game. restart. ")
    elif answer == "no":
        print("As You guys are too scared to go in, You and your friends hide in a bush on the side of the abandoned building. You guys here the Old looking granny coming in the distance. Then complete silence. You pick up your head to check where she went. Then out of now where the granny comes falling out of the sky and lands right in front of you. You are petrified. Then with one scope, the granny picks you up with no problem and throws you across the woods. You hit the trees and black out. Time passes and then you wake up. All you see is white. You are in Heaven. You lost the game. restart.")


else:
    print("Try Again!")