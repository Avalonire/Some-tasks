def ctz(name, age, city):
    return print(f'{name}, {age} год(а), проживает в городе {city}')


ctz('Alex', 30, 'Москва')
print('-' * 100)

numbers = [1, 2, 44, 545, 2, 45]
numbers_2 = [23, 12, 33, 1, 56, 77]


def num(list):
    return max(list)


print(num(numbers))
print('-' * 100)

name = input('Введите имя персонажа: ')
lvl = input('Введите уровень персонажа: ')
health = 100
damage = 50
armor = 1.2


def lvl_up(lvl):
    for i in range(int(lvl) - 1):
        global health, damage, armor
        health += 50
        damage += 20
        armor *= 1.4


if 10 > int(lvl) > 1:
    lvl_up(int(lvl))

print(f'Имя: {name}, Здоровье: {health}, Урон: {damage}, Защита: {armor}')

player = {name: name, health: health, damage: damage, armor: armor}
goblin = {name: 'Goblin', health: 40, damage: 30, armor: 0}
orc = {name: 'Orc', health: 100, damage: 40, armor: 1.3}


def attack(attacker, defender):
    def dmg_reduce(dmg, armor):
        if defender[armor] != 0:
            return dmg / armor
        else:
            return dmg

    damage_final = dmg_reduce(attacker[damage], defender[armor])
    defender[health] -= round(damage_final)
    if defender[health] <= 0:
        print(f'{name} ударил {defender[name]} на {attacker[damage]}, {defender[name]} МЕРТВ!')
    else:
        print(
            f'{name} ударил {defender[name]} на {round(damage_final)}, у {defender[name]} осталось {defender[health]} здоровья')


if str(input('Кого атакуешь? (goblin, orc): ')) == 'goblin':
    attack(player, goblin)
else:
    attack(player, orc)
