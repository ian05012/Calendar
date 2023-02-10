import json

itt = {}


def add(key, value):
    if not itt.keys().__contains__(key):
        itt[key] = [value]
    else:
        itt[key].append(value)

    save()


def delete(key, num):
    print(num)
    del itt[key][num]
    if len(itt[key]) == 0:
        del itt[key]

    save()


def load():
    global itt
    itt = json.load(open('data.json', 'r+'))


def save():
    global itt

    with open('data.json', 'r+') as file:
        file.truncate(0)
        file.seek(0)
        json.dump(itt, file, indent=2)


def getIttValue(key):
    if not itt.keys().__contains__(key):
        return 0
    else:
        return itt[key]
