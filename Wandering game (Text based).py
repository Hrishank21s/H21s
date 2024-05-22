print(
    "You stand at the edge of an ancient stone bridge. The misty forest surrounds you, and the sound of a nearby river rushing below fills your ears.")
print(
    "You've heard rumors of a mystical village named Eldoria hidden deep within these woods. Your journey to find this village has been long and arduous, but you sense that you're close.")
print(
    "To your right, a narrow path leads into the dense forest. The bridge before you stretches across the river, leading to a shadowy land beyond.")
choice = input(
    "Do you:\n1. Take the right path into the forest.\n2. Cross the bridge to explore the shadowy land.\nType '1' or '2' to make your choice: ")
if choice == "1":
    print(
        "You decide to take the right path into the forest. The trees grow thicker, and the light dims as you venture deeper. The forest is eerily quiet, except for the occasional rustling of leaves.")
    print("Suddenly, you come across an old wooden signpost pointing in two directions.")
    print("The sign reads:\n- Left: Toward Eldoria.\n- Right: To the Enchanted Grove.")
    choice = input(
        "Do you:\n1. Follow the sign toward Eldoria.\n2. Head toward the Enchanted Grove.\nType '1' or '2' to make your choice: ")
    if choice == "1":
        print(
            "You follow the sign pointing toward Eldoria. After walking for what feels like hours, you finally reach a clearing. There, nestled between the trees, is the village of Eldoria.")
        print("The village is bustling with activity; children play in the streets, and merchants sell their wares.")
        print(
            "You notice an elderly woman sitting by a well, weaving a tapestry that glows with a magical light. She looks up and beckons you over.")
        choice = input(
            "Do you:\n1. Approach the elderly woman and ask for guidance.\n2. Explore the village on your own.\nType '1' or '2' to make your choice: ")
        if choice == "1":
            print(
                "You approach the elderly woman by the well. She looks up at you with kind, knowing eyes. 'Ah, a seeker of Eldoria,' she says with a smile. 'I can see the questions in your eyes. This village holds many secrets, but not all are meant to be found. What is it you seek?'")
            choice = input(
                "Do you:\n1. Ask about the village's secrets.\n2. Request directions to a specific location within Eldoria.\nType '1' or '2' to make your choice: ")
            if choice == "1":
                print(
                    "You ask the elderly woman about the village's secrets. She smiles and begins to tell you the tales of Eldoria's hidden treasures and ancient magic.")
                # Continue the story from here
            elif choice == "2":
                print(
                    "You request directions to a specific location within Eldoria. The elderly woman points you towards the village center where a grand library stands.")
                # Continue the story from here
            else:
                print("Invalid choice. The adventure ends here.")
        elif choice == "2":
            print(
                "You decide to explore the village on your own. The streets are lively, filled with the sound of laughter and music. As you wander, you come across a bustling market square. Various stalls offer exotic goods and magical items.")
            print("A mysterious merchant catches your eye, his stall adorned with rare artifacts.")
            choice = input(
                "Do you:\n1. Approach the merchant and inquire about his wares.\n2. Continue exploring the market square.\nType '1' or '2' to make your choice: ")
            if choice == "1":
                print(
                    "You approach the merchant and inquire about his wares. He shows you a collection of rare and magical artifacts, each with its own unique history.")
                # Continue the story from here
            elif choice == "2":
                print(
                    "You continue exploring the market square, taking in the sights and sounds of Eldoria's vibrant market.")
                # Continue the story from here
            else:
                print("Invalid choice. The adventure ends here.")
        else:
            print("Invalid choice. The adventure ends here.")
    elif choice == "2":
        print(
            "You decide to head toward the Enchanted Grove. As you walk, the trees become more vibrant, their leaves shimmering with a magical glow. The air is filled with the scent of flowers and the sound of birds singing.")
        print(
            "In the heart of the grove, you find a crystal-clear pond with a beautiful, glowing flower at its center. As you approach, a soft voice whispers in your ear, 'Pluck the flower and you will be granted a wish.'")
        choice = input(
            "Do you:\n1. Pluck the flower and make a wish.\n2. Leave the flower untouched and continue exploring.\nType '1' or '2' to make your choice: ")
        if choice == "1":
            print(
                "You gently pluck the glowing flower from the pond. As you hold it, you feel a surge of magical energy. 'What is your wish?' the soft voice whispers again.")
            choice = input(
                "Do you:\n1. Wish for knowledge of Eldoria's secrets.\n2. Wish for a safe and prosperous journey.\nType '1' or '2' to make your choice: ")
            if choice == "1":
                print(
                    "You wish for knowledge of Eldoria's secrets. Instantly, your mind is filled with ancient lore and hidden truths about the mystical village.")
                # Continue the story from here
            elif choice == "2":
                print(
                    "You wish for a safe and prosperous journey. A warm light envelops you, filling you with a sense of safety and well-being.")
                # Continue the story from here
            else:
                print("Invalid choice. The adventure ends here.")
        elif choice == "2":
            print(
                "You decide to leave the flower untouched and continue exploring the grove. The beauty of the grove is mesmerizing, and you feel a sense of peace here. As you wander, you come across an ancient tree with intricate carvings.")
            print("The carvings depict a map leading to a hidden treasure within the grove.")
            choice = input(
                "Do you:\n1. Follow the map to find the hidden treasure.\n2. Sit by the tree and meditate, seeking guidance.\nType '1' or '2' to make your choice: ")
            if choice == "1":
                print(
                    "You decide to follow the map to find the hidden treasure. After a short walk, you discover a hidden chest filled with gold and precious gems.")
                # Continue the story from here
            elif choice == "2":
                print(
                    "You sit by the tree and meditate, seeking guidance. A feeling of calm washes over you, and you gain a deeper understanding of the grove's magic.")
                # Continue the story from here
            else:
                print("Invalid choice. The adventure ends here.")
        else:
            print("Invalid choice. The adventure ends here.")
    else:
        print("Invalid choice. The adventure ends here.")
elif choice == "2":
    print(
        "You decide to cross the bridge to explore the shadowy land. As you walk across the ancient stone bridge, you hear the creaking of old wood and the murmuring of the river below.")
    print(
        "Once on the other side, you find yourself in a dark, mist-covered valley. The air is colder here, and a sense of unease settles over you. In the distance, you see a flickering light.")
    choice = input(
        "Do you:\n1. Head toward the flickering light.\n2. Stay and explore the immediate area.\nType '1' or '2' to make your choice: ")
    if choice == "1":
        print(
            "You head toward the flickering light. As you draw nearer, you realize it's coming from a small, cozy cottage. The door creaks open slightly, and a warm, inviting light spills out. A kindly old man appears at the door and smiles at you.")
        print("'Welcome, traveler. What brings you to this forsaken land?' he asks.")
        choice = input(
            "Do you:\n1. Tell him about your quest to find Eldoria.\n2. Ask him for shelter and rest.\nType '1' or '2' to make your choice: ")
        if choice == "1":
            print(
                "You tell the old man about your quest to find Eldoria. He nods thoughtfully. 'Eldoria is a place of great wonder and magic,' he says. 'But it's not easy to find. I can offer you a map that might help, but it comes at a price.'")
            choice = input(
                "Do you:\n1. Accept the map and agree to his terms.\n2. Politely decline and ask for more information.\nType '1' or '2' to make your choice: ")
            if choice == "1":
                print(
                    "You accept the map and agree to his terms. The old man hands you a worn, ancient map that shows the way to Eldoria.")
                # Continue the story from here
            elif choice == "2":
                print(
                    "You politely decline and ask for more information. The old man shares some of his knowledge about the land and the challenges you might face.")
                # Continue the story from here
            else:
                print("Invalid choice. The adventure ends here.")

