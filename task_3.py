world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022]='Аргентина'

for key, value in world_champions.items():
    print(f"{key} - {value}")

is_exist = False
country = 'Италия'
for key, value in world_champions.items():
    if (value == country) and (key >= 2000):
        is_exist=True
 

if is_exist:
     print(f"{country} cтановилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country} не выигрывала чемпионат мира по футболу в 21 веке.")

