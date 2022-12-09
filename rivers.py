rivers = {
    "nile": "egypt",
"amazon river": "brazil",
"mississippi river": "the united states", 
    }


print("All rivers:")
for river in rivers.keys():
    print(river.title())


print("All countries:")
for country in rivers.values():
    print(country.title())


for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")