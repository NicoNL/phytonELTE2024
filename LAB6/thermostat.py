# Code cell 11
def smart_thermostat(temp, people_in):
    if temp < 23  and people_in:
        return "Heating on"
    elif temp >= 23 or not people_in:
        return "Heating off"

print(smart_thermostat(21,False))
print(smart_thermostat(21,True))