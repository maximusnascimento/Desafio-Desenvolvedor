def inverter(string):
    letras = []
    for i in string:
        letras = [i] + letras

    return letras

string = input()
print(inverter(string))