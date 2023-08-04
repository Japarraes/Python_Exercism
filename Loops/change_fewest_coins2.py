import sys

# CON RECURSIVIDAD
def find_fewest_coins(coins, target):
# Función # para encontrar el número mínimo de monedas requeridas
# para obtener un total de `target` del conjunto `S`

    # si el total es 0, no se necesitan monedas
    if target == 0:
        return 0

    # devuelve infinito si el total se vuelve negativo
    if target < 0:
        return sys.maxsize

    # inicializa el número mínimo de monedas necesarias hasta el infinito
    min_coins = sys.maxsize

    # hacer por cada moneda
    for c in coins:

        # recurre para ver si se puede alcanzar el total incluyendo la moneda actual `c`
        result = find_fewest_coins(coins, target - c)

        # actualice la cantidad mínima de monedas necesarias si elige el actual
        # La moneda # resultó en una solución
        if result != sys.maxsize:
            min_coins = min(min_coins, result + 1)

    # devuelve la cantidad mínima de monedas necesarias
    return min_coins

# print(find_fewest_coins([1, 5, 10, 25], 1))                  # [1]
# print(find_fewest_coins([1, 5, 10, 25, 100], 25))            # [25]
print(find_fewest_coins([1, 5, 10, 25, 100], 15))            # [5, 10]
# print(find_fewest_coins([1, 4, 15, 20, 50], 23))             # [4, 4, 15]
# print(find_fewest_coins([1, 5, 10, 21, 25], 63))             # [21, 21, 21]
# print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 999))    # [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100]
# print(find_fewest_coins([2, 5, 10, 20, 50], 21))             # [2, 2, 2, 5, 10]
# print(find_fewest_coins([4, 5], 27))                         # [4, 4, 4, 5, 5, 5]
# print(find_fewest_coins([1, 5, 10, 21, 25], 0))              # []
# print(find_fewest_coins([5, 10], 3))                         # "can't make target with given coins")
# print(find_fewest_coins[5, 10], 94)                          # "can't make target with given coins")
# print(find_fewest_coins([1, 2, 5], -5))                      # "target can't be negative")
