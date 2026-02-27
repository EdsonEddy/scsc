
import math

# Función de redondeo similar a Java/C
def round_java_c_style(value, decimals):
    factor = 10 ** decimals
    return math.floor(value * factor + 0.5) / factor

def calculate_fruit_percentages(n, cases):
    results = []

    for i in range(n):
        fruits = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        case = cases[i]
        total = len(case)

        for c in case:
            if c in fruits:
                fruits[c] += 1

        result = f"Caso {i + 1}:"
        for char, count in fruits.items():
            percentage = (count * 100.0) / total
            rounded_percentage = round_java_c_style(percentage, 2)
            result += f"\n{char}= {rounded_percentage:.2f}"
        
        results.append(result)
    
    return results

# Ejemplo de uso
n = int(input())
cases = [input().strip() for _ in range(n)]
results = calculate_fruit_percentages(n, cases)

for result in results:
    print(result)
