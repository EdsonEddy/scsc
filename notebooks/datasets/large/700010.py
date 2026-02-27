def java_style_round(n, decimals=2):
    multiplier = 10 ** decimals
    return (int(n * multiplier + 0.5)) / multiplier

def calcular_porcentajes(cultivos):
    frutas = ['a', 'e', 'i', 'o', 'u']
    total = len(cultivos)
    
    conteo_frutas = {fruta: 0 for fruta in frutas}
    
    for c in cultivos:
        if c in frutas:
            conteo_frutas[c] += 1
    
    porcentajes = {fruta: (conteo_frutas[fruta] / total) * 100 if total > 0 else 0.0 for fruta in frutas}
    
    porcentajes_redondeados = {fruta: java_style_round(porcentajes[fruta], 2) for fruta in frutas}
    
    return porcentajes_redondeados

def main():
    T = int(input().strip())
    
    for t in range(1, T + 1):
        S = input().strip()
        porcentajes = calcular_porcentajes(S)
        
        print(f'Caso {t}:')
        for fruta, porcentaje in porcentajes.items():
            print(f'{fruta}= {porcentaje:.2f}')

if __name__ == "__main__":
    main()