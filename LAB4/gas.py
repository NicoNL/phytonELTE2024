mil2km = 1.609344
gal2lit = 3.785411784

def liter_100km_to_gallon(liter):
    miles_per_100km = 100 / mil2km    
    mpg = miles_per_100km / (liter / gal2lit)    
    return mpg

def gallon_100km_to_liter(miles):
    gpm = 100/miles
    gp100km = gpm/mil2km
    lp100km = gp100km*gal2lit
    return lp100km

x = float(input("Please enter a number:\n"))
print(liter_100km_to_gallon(x), " mpg")

y = float(input("Please enter a number:\n"))
print(gallon_100km_to_liter(y), " kpl")

