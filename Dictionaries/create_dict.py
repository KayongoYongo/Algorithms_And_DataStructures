#!/usr/bin/python3

# A dictionary can be initialized in two ways
champions_league = {}
europa_league = dict()

champions_league = {
    'England':'Manchester City',
    'Spain':'Barcelona',
    'Italy':'Inter Milan',
    'Germany':'Borrusia Dortmound',
    'France':'Lens'
}

europa_league = dict([
    ('England', 'Brighton'),
    ('Spain', 'Real Betis'),
    ('Italy', 'Lazio'),
    ('Germany', 'Bayern Leverkusen'),
    ('France', 'Olympic Lyon')
])

print(champions_league)
print(europa_league)
