# reviewer: Netta.
def isleap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


assert isleap(2000) == True
for leap in range(1000, 2201, 100):
    print(f'The year: {leap}. leap: {isleap(leap)}')
