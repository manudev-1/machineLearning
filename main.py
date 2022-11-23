import pandas
from csv import writer
from sklearn.tree import DecisionTreeClassifier
import datetime

# Prende il Genere in INPUT
def checkGender():
    try:
        gender = int(input("Enter a gender: 0(Female) 1(Male)\n"))
        if gender == 0 or gender == 1:
            print(f"Gender: {gender}")
        else:
            print(f"The entered gender is not valid!")
        while gender != 0 and gender != 1:
            gender = int(input("Enter a gender: 0(Female) 1(Male)\n"))
            try:
                if gender == 0 or gender == 1:
                    print(f"Gender: {gender}")
                else:
                    print(f"The entered gender is not valid!")
            except ValueError as ve:
                print(f"You entered {gender}, which is not a number!")
        return gender
    except ValueError as ve:
        print("You entered something, which is not a number!")
        return

# Prende l'Età in INPUT
def checkAge():
    today = datetime.date.today()
    try:
        age = int(input("Enter an age:\n"))
        if age != None:
            if today.year - age >= 1950 and age > 0:
                print(f"Age: {age}")
            else:
                print(f"{age} is not valid!")
        while today.year - age <= 1950 or age <= 0:
            age = int(input("Enter an age:\n"))
            try:
                if age != None:
                    if today.year - age >= 1950 and age > 0:
                        print(f"Age: {age}")
                    else:
                        print(f"{age} is too big!")
            except ValueError as ve:
                print(f"You entered {age}, which is not a number")
        return age
    except ValueError as ve:
        print("You entered something, which is not valid!")
        return

# Predizione del dato
def machinLearning():
    gender = checkGender()
    if gender == None: return
    age = checkAge()
    if age == None: return
    trainingSet = pandas.read_csv('trainingSet.csv')
    x = trainingSet.drop(columns=['videogame'])
    y = trainingSet['videogame']

    model = DecisionTreeClassifier()
    model.fit(x.values, y.values)
    return model.predict([[gender, age]])

# Aggiungi un nuovo Dato
def addData():
    data = []
    gender = checkGender()
    age = checkAge()
    categoryList = ["sparatutto", "platform", "combattimento", "fantasy", "gestionale"]
    print("Choice from the Menù the category:\n")
    for c in categoryList:
        print(f"- [{c[0].capitalize()}] {c.capitalize()}")

    choice = input("Choice digiting the first letter:\n")
    choice = choice.capitalize()
    # Problema di EFFICIENZA
    while choice.isnumeric() or len(choice) != 1 or choice != "S" and choice != "P" and choice != "C" and choice != "F" \
            and choice != "G":
        choice = input(f"You entered \'{choice}\', which is not valid, Re-enter it:\n")
        choice = choice.capitalize()
    if len(choice) == 1:
        for c in categoryList:
            if choice == c[0].capitalize():
                cDef = c
                data.append(gender)
                data.append(age)
                data.append(cDef)
                with open('trainingSet.csv', 'a', newline='') as file:
                    writerFile = writer(file)
                    writerFile.writerow(data)
                    file.close()
                print("The data has been taken")
                __init__()
                return

def __init__(): #Init funcion
    # Menu
    print('''
  __  __            _     _              _                           _               __  __                  
 |  \/  |          | |   (_)            | |                         (_)             |  \/  |                 
 | \  / | __ _  ___| |__  _ _ __   ___  | |     ___  __ _ _ __ _ __  _ _ __   __ _  | \  / | ___ _ __  _   _ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \ | |    / _ \/ _` | '__| '_ \| | '_ \ / _` | | |\/| |/ _ \ '_ \| | | |
 | |  | | (_| | (__| | | | | | | |  __/ | |___|  __/ (_| | |  | | | | | | | | (_| | | |  | |  __/ | | | |_| |
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___| |______\___|\__,_|_|  |_| |_|_|_| |_|\__, | |_|  |_|\___|_| |_|\__,_|
                                                                              __/ |                          
                                                                             |___/                               
    \nSelect the action from the menù: \n[1]: Add data\n[2]: Use the AI\n[3]: Quit''')

    try:
        sel = int(input("Make your choice:\n"))
        while len(str(sel)) != 1:
            sel = int(input("Remake your choice:\n"))
        if len(str(sel)) == 1:
            match sel:
                case 1:
                    print("You chose \'Add data\'")
                    print(addData())
                case 2:
                    print("You chose \'Use the AI\'")
                    print(machinLearning())
                    __init__()
                case 3:
                    print("You chose \'Quit\'")
                    return
    # Errore di Valore
    except ValueError as ve:
        print(f"You enterd something, which is not a valid choose")
        return

#Inizio Programma
if __name__ == '__main__':
    print(__init__())