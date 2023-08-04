import sys

# SIN USAR RECURSIVIDAD
def find_fewest_coins(coins, target):
    # `T[i]` almacena el número mínimo de monedas necesarias para obtener un total de i
    T = [0] * (target + 1)

    for i in range(1, target + 1):

        # inicializa el número mínimo de monedas necesarias hasta el infinito
        T[i] = sys.maxsize

        # hacer por cada moneda
        for c in range(len(coins)):
            # comprobar si el índice no se vuelve negativo incluyendo
            # moneda actual `c`
            if i - coins[c] >= 0:
                result = T[i - coins[c]]

                # si se puede alcanzar el total incluyendo la moneda actual `c`,
                # actualiza el número mínimo de monedas necesarias `T[i]`
                if result != sys.maxsize:
                    T[i] = min(T[i], result + 1)

    # `T[target]` almacena el número mínimo de monedas necesarias para obtener un total de `target`
    return T[target]

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
