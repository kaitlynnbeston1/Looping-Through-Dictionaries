# Making the glossary
glossary = {
    "conditional test": "a test where Python checks whether something is true or false.",
    "print statement": "a function in Python which prints text to a terminal.",
    "list": "A list of strings, intigers, and/or floats in Python. Allows you to do things like find the sum of a bunch of items or easily pull items for other perposes. See string, intiger, and floating point.",
    "for loop": "A loop in Python that does something for every item in a list.",
    "tuple": "Similar to a list, only items within a tuple cannot be modified.",
    }


# Adding more items to the glossary.
glossary["string"] = "A data type consisting of letters or numbers. Strings will primarily only have letters or a combonation of both letters and numbers unless using the input function."
glossary["intiger"] = "Numbers which do not have a decimal point. For example, 32 or 71."
glossary["floating point"] = "Numbers which have a decimal point. Examples include 6.0 or 3.14. Can also just be refered to as floats."
glossary["elif"] = "When working with if statements, elif acts as else and if combined. Useful for chains of if statements. See If Statement(s) for more details."
glossary["if statement(s)"] = "If a conditional test is true, do an action. See conditional test for more information."


# printing

for word, define in sorted(glossary.items()):
    print(f"{word.title()}: \n {define} \n \n")