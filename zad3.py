import matplotlib.pyplot as plt
import numpy as np

# 1. Diagram Bifurkacji
def bifurcation_diagram():
    mu_values = np.linspace(2.5, 4.0, 1000)
    x = 0.5 * np.ones_like(mu_values)
    
    # Iteracje wstępne (odrzucamy stany przejściowe)
    for _ in range(100):
        x = mu_values * x * (1 - x)
        
    # Rysowanie diagramu
    plt.figure(figsize=(10, 6))
    for _ in range(200): # Zbieramy punkty atraktora
        x = mu_values * x * (1 - x)
        plt.plot(mu_values, x, ',k', alpha=0.1) # ,k to małe kropki
        
    plt.title("Diagram bifurkacji funkcji logistycznej")
    plt.xlabel("Parametr mu")
    plt.ylabel("Wartości x")
    plt.xticks(np.arange(2.5, 4.05, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)
    plt.savefig("bifurkacja.png") # Zapis do pliku
    plt.show()

# 2. Orbita dla wybranego mu
def plot_orbit(mu, x0, n_iter=20):
    x = x0
    trajectory = [x]
    print(f"\n--- ZADANIE 3: Orbita dla mu={mu}, x0={x0} ---")
    print(f"Iter 0: {x}")
    for i in range(1, n_iter + 1):
        x = mu * x * (1 - x)
        trajectory.append(x)
        print(f"Iter {i}: {x:.4f}\n")
    
    plt.figure(figsize=(8, 4))
    plt.plot(range(n_iter + 1), trajectory, 'o-')
    plt.title(f"Orbita układu dla mu={mu}")
    plt.xlabel("Iteracja")
    plt.ylabel("Wartość x")
    plt.xticks(range(n_iter + 1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)
    plt.savefig("orbita.png")
    plt.show()

# Wykonanie
bifurkacja = bifurcation_diagram()

# Dobór mu: > 3, ale przed kolejną bifurkacją (która jest ok 3.45)
# Wybieramy mu = 3.2
plot_orbit(mu=3.2, x0=0.25, n_iter=20)