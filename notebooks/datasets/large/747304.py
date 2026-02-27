def count(text, letra):
    count = 0
    for i in range(len(text)):
        if text[i] == letra:
            count+=1
    return count

def plant_porcent(text):
    dic = {
        "a" : 0.00,
        "e" : 0.00,
        "i" : 0.00,
        "o" : 0.00,
        "u" : 0.00
    }

    for i in dic:
        porcent = count(text, i)/len(text)*100
        dic.update({i : porcent})
    return dic

def round_java_style_two_decimals(value):
    if value > 0:
        return int(value * 100 + 0.5) / 100
    else:
        return int(value * 100 - 0.5) / 100


for i in range(int(input())):
    plant = input()
    dicti = plant_porcent(plant)
    print(f"Caso {i+1}:")
    for i, y in dicti.items():
        print(f'{i}= {"{:.2f}".format(round_java_style_two_decimals(y))}')
