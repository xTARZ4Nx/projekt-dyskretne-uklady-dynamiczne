import random
import numpy as np
import matplotlib.pyplot as plt

def sierpinski_chaos_game(n_points=50000):
    # Wierzchołki trójkąta
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3)/2])
    
    # Jawne wzory na kontrakcje (skalowanie o 0.5 i przesunięcie)
    # f(x,y) = 0.5 * [x,y] + przesunięcie
    transforms = [
        lambda p: 0.5 * p,            # Przesunięcie do p1 (0,0) jest zerowe
        lambda p: 0.5 * p + 0.5 * p2, # W stronę p2
        lambda p: 0.5 * p + 0.5 * p3  # W stronę p3
    ]
    
    # Stała Lipschitza dla każdej transformacji
    lipschitz_s = 0.5
    
    # Gra w chaos
    point = np.array([0.5, 0.5]) # Punkt startowy
    x_coords = []
    y_coords = []
    
    for _ in range(n_points):
        # Losujemy transformację z prawdopodobieństwem 1/3 (rozkład klasyczny)
        func = random.choice(transforms)
        point = func(point)
        
        x_coords.append(point[0])
        y_coords.append(point[1])
        
    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, s=0.2, c='blue')
    plt.title("Trójkąt Sierpińskiego - Gra w Chaos")
    plt.axis('equal')
    plt.axis('off')
    plt.savefig("sierpinski.png")
    plt.show()
    
    return lipschitz_s, len(transforms)

s, N = sierpinski_chaos_game()
fractal_dim = np.log(N) / np.log(1/s)
print(f"\n--- ZADANIE 4 ---")
print(f"Stała Lipschitza s: {s}")
print(f"Liczba przekształceń N: {N}")
print(f"Wymiar fraktalny D: {fractal_dim:.4f}\n")