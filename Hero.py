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


Hero = SuperHero('Bruce', 'Batman', 'Money', 100, 'This city needs a new hero')

Hero.double_health()
Hero.display_name()
print(Hero)
print(f'The length of catchphrase is: {len(Hero)}')
