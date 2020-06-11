human_data = {}
droid_data = {}

import json

class Human():
    def __init__(self, id, name, friends, appears_in, home_planet):
        self.id = id
        self.name = name
        self.friends = friends
        self.appears_in = appears_in
        self.home_planet = home_planet



class Droid():
    def __init__(self, id, name, friends, appears_in, primary_function):
        self.id = id
        self.name = name
        self.friends = friends
        self.appears_in = appears_in
        self.primary_function = primary_function

# global human_data, droid_data
luke = Human(
    id="1000",
    name="Luke Skywalker",
    friends=["1002", "1003", "2000", "2001"],
    appears_in=[4, 5, 6],
    home_planet="Tatooine",
)

vader = Human(
    id="1001",
    name="Darth Vader",
    friends=["1004"],
    appears_in=[4, 5, 6],
    home_planet="Tatooine",
)

han = Human(
    id="1002",
    name="Han Solo",
    friends=["1000", "1003", "2001"],
    appears_in=[4, 5, 6],
    home_planet=None,
)

leia = Human(
    id="1003",
    name="Leia Organa",
    friends=["1000", "1002", "2000", "2001"],
    appears_in=[4, 5, 6],
    home_planet="Alderaan",
)

tarkin = Human(
    id="1004",
    name="Wilhuff Tarkin",
    friends=["1001"],
    appears_in=[4],
    home_planet=None,
)

human_data = {
    "1000": luke,
    "1001": vader,
    "1002": han,
    "1003": leia,
    "1004": tarkin,
}

c3po = Droid(
    id="2000",
    name="C-3PO",
    friends=["1000", "1002", "1003", "2001"],
    appears_in=[4, 5, 6],
    primary_function="Protocol",
)

r2d2 = Droid(
    id="2001",
    name="R2-D2",
    friends=["1000", "1002", "1003"],
    appears_in=[4, 5, 6],
    primary_function="Astromech",
)

droid_data = {"2000": c3po, "2001": r2d2}


def get_character(id):
    return human_data.get(id) or droid_data.get(id)


def get_friends(character):
    return map(get_character, character.friends)


# to fetch required objects along with its fields from the data schema
def get_information(field_name, arguments, selections_set):
    objects = []
    error_message = ''
    error_occured = False
    object_data = {}

    if field_name == 'hero':
        object_data = human_data
    elif field_name == 'droid':
        object_data = droid_data
    else:
        error_occured = True
        error_message = 'Cannot query field ' + field_name + ' - Object does not exist in database'

    for key, value in object_data.items():
        objects.append(value)

    for key, value in arguments.items():
        # print('value: ',value, '  type of value: ', type(value))
        # hero = human_data.get(value)

        obj_removal_index = []
        i = 0
        for obj in objects:
            try:
                if ""+str(getattr(obj, key)) != ''+str(value):
                    obj_removal_index.append(i)
                i += 1
            except AttributeError:
                error_message = 'Invalid Argument ' + key + '!'
                error_occured = True
                break
        if error_occured:
            break

        for index in sorted(obj_removal_index, reverse=True):
            objects.pop(index)

    result_objects = []

    try:
        for obj in objects:
            result = {}
            for field in selections_set:
                result[field] = getattr(obj, field)
            result_objects.append(result)
    except AttributeError:
        error_message = 'Attribute does not exist!'
        error_occured = True

    return result_objects, error_occured, error_message


def get_human(id):
    return human_data.get(id)


def get_droid(id):
    return droid_data.get(id)
