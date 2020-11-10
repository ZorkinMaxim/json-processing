import json

def menu(title, options):
    print(f'##### {title:^15} #####')
    for k in options:
        print(f'{k}. {options[k]}')
    print(f'##### {"Choose Option":^15} #####')

    selected = int(input('>>'))
    if selected not in options:
        print('Wrong option!')
    return selected


def loadEventData():
    file = open("data\event.json")
    data = json.load(file)
    return data

def printEvent(data):
    print("#" * 27)
    print(f"Event: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Date: {len(data['guests'])}")
    print("#" * 27)

def inviteGuest(data):
    name = input("Enter guest name: ")
    data["guests"].append(name)
    print(f"The guest '{name}' was successfully registered!")
    return data

def removeGuest(data):
    name = input("Enter name of registered guest: ")
    if name in data['guests']:
        data['guests'].remove(name)
        print(f"The guest '{name}' was successfully removed!")
    else:
        print(f'Error! The name "{name}" DOES NOT exists!')
    return data

def saveData(data):
    file = open("data\event.json","w")
    json.dump(data, file)
    file.close()

#guests = loadEventData()
##############################################

while True:
    result = menu('Main', {
        1: 'View all guests',
        2: 'Add guest',
        3: 'Remove guest',
        0: 'Exit'
    })

    if result == 1:
        data = loadEventData()
        printEvent(data)
        print(f"All registered Guests: {data['guests']}")
    if result == 2:
        data = loadEventData()
        data = inviteGuest(data)
        saveData(data)
    if result == 3:
        data = loadEventData()
        data = removeGuest(data)
        saveData(data)
    if result == 0:
        print("Thank you!")
        break



# data = loadEventData()
# printEvent(data)
# data = inviteGuest(data)
# printEvent(data)
# saveData(data)