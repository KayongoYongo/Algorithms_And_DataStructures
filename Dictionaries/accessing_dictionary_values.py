#!/usr/bin/python3

# A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):
champions_league = {
    'England':'Manchester City',
    'Spain':'Barcelona',
    'Italy':'Inter Milan',
    'Germany':'Borrusia Dortmound',
    'France':'Lens'
}

print(champions_league['Spain'])
print(champions_league['Germany'])
print('The last key element will generate a key error since the key value doesn\'t exist')
print(champions_league['Portugal'])
