# Original code
favorite_languages ={
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }


# Appending all keys to a list
people = []
for person in favorite_languages.keys():
    people.append(person)


# adding new people to the list
people.append("anakin")
people.insert(2, "threepio")
people.insert(0, "yoda")


# Checking the list for respondants
for person in people:
    if person not in favorite_languages.keys():
        print(f"{person}, would you like to respond to my poll?")
    else:
        print(f"Thank you for responding to the poll, {person}!")