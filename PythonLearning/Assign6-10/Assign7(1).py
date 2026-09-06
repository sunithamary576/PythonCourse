dict={
    "Tumkur":"Thatte idli",
    "Banglore":"Meghanas biriyani",
    "Mysore":"Mysore bonda",
    "Dharwad":"Dharwad peda",
    "Manglore":"Kori roti"
}
print(dict)

dict["Madikeri"]="Tawa fry"
print("\nAdding a new city and its dish to the dictionary...\n")
print(dict)

dict["Banglore"]="Masala Dosa"
print("\nUpdating...\n")
print(dict)

dict.pop("Madikeri")
print(dict)
print(dict.keys())
print(dict.values())