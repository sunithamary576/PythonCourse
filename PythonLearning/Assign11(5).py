cities={
    "Tumkur": 9,
    "Mysore": 15, 
    "Bengaluru": 25, 
    "Manglore": 11, 
    "Hassan": 7
}
new={city:pop for city,pop in cities.items() if pop<10}
print(new)