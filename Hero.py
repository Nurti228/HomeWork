class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(self.name)

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Nickname: {self.nickname}, Superpower: {self.superpower}, Health points: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def new_phrase(self):
        return 'True in the True_phrase'


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def new_phrase(self):
        return 'True in the True_phrase'


class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, target):
        target.health_points -= self.damage


Hero = SuperHero('Bruce', 'Batman', 'Money', 100, 'This city needs a new hero')
air_hero = AirHero('Clark', 'Superman', 'superpower', 170, 'Truth, Justice and better Tomorrow', 50)
earth_hero = EarthHero('Peter', 'SpiderMan', 'spider', 150, 'With great power comes great responsibility', 25)
villain = Villain('Dark Lord', 'the Destroyer', 'gravity', 500, 'Embrace the darkness!', 100)

Hero.double_health()
Hero.display_name()
print(Hero)
print(f'The length of catchphrase is: {len(Hero)}')

air_hero.double_health()
print(air_hero.new_phrase())

earth_hero.double_health()
print(earth_hero.new_phrase())

print(villain.people)
villain.gen_x()
villain.crit(air_hero)
print("AirHero's health points:", air_hero.health_points)