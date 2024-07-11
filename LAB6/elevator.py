# Code cell 17
class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = floor_numbers
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        if floor_type in self._floor_types:
            print('The {} floor is the number: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('There is no {} floor in this building.'.format(floor_type))
    
    def go_to_floor(self, floor_number):
        if floor_number in self._floor_numbers:
             print("Going to the ",  self._number_to_type_dict[floor_number], " floor")
        else:
            print("There is no ", floor_number, " floor in this builder")


floor_types = ['Parking', 'Shops', 'Food Court', 'Offices', 'Reception']
floor_numbers = range(-1,3)
el = Elevator(floor_numbers, floor_types)
el.go_to_floor(1)
el.go_to_floor(-2)
el.ask_which_floor('Offices')
el.ask_which_floor('Swimming Pool')