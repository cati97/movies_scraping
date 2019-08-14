# [x] ask user to input 3 friends - using split(", ")
# [x] if user_input is in people.txt tell user - "{friend} leaves nearby"
# [x] open people.txt and readlines() - returns a list in which each element is a line
# [x] write into nearby_friends.txt only friends that are nearby (that match)


friends = input("Enter three of your friends using comma: ").split(", ")
friends_lower = [f.lower() for f in friends]

people_file = open('people.txt', 'r')
people_list_stripped_lower = [element.strip().lower() for element in people_file.readlines()]  # split("\n")!!
# strip() eliminates all white spaces/tabs/new lines before and after a string

people_file.close()

nearby_file = open('nearby_friends.txt', 'w')

for friend in friends_lower:
    if friend in people_list_stripped_lower:
        print(friend.capitalize() + " lives nearby")
        nearby_file.write(f"{friend.capitalize()}\n")

nearby_file.close()











