import numpy as np

# Dane z treści zadania
L = np.array([
    [0, 2, 3, 0],
    [0.3, 0, 0, 0],
    [0, 0.49, 0, 0],
    [0, 0, 0.3, 0]
])

N0 = np.array([1000, 2000, 1500, 500])

# 1. Rozkład po 10 latach
N10 = np.linalg.matrix_power(L, 10) @ N0

# 2. Analiza długoterminowa (wartości własne)
eigenvalues, eigenvectors = np.linalg.eig(L)
lambda_max = max(abs(eigenvalues))

# 3. Dobór parametru uboju (h)
# Aby populacja była stabilna, dominująca wartość własna musi wynosić 1
# Nowa macierz L_new = h * L, więc jej wart. wł. to h * lambda_max
# Chcemy h * lambda_max = 1 => h = 1 / lambda_max
h = 1 / lambda_max

print("--- ZADANIE 1 ---")
print(f"\nPopulacja po 10 latach: {N10}")
print(f"Suma populacji po 10 latach: {np.sum(N10):.0f}")
print(f"Dominująca wartość własna (lambda_max): {lambda_max:.4f}")
print(f"Współczynnik uboju (h) dla stabilizacji: {h:.4f}")
print(f"Procent populacji do pozostawienia: {h*100:.2f}%\n")