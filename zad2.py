import numpy as np
from scipy.optimize import fsolve

# Parametry stałe
b = 1.1e6
r = 8
s = 16

def lasota_func(c, a):
    return (1 - a) * c + b * (c**r) * np.exp(-s * c)

def derivative_lasota(c, a):
    # Pochodna analityczna f'(c)
    # f'(c) = (1-a) + b * [ r*c^(r-1)*e^(-sc) + c^r * (-s)*e^(-sc) ]
    term1 = 1 - a
    term2 = b * np.exp(-s * c) * (r * c**(r - 1) - s * c**r)
    return term1 + term2

def analyze_stability(a_val):
    print(f"\nAnaliza dla a = {a_val}:")
    
    # Szukamy punktów stałych: f(c) = c => f(c) - c = 0
    equation = lambda c: lasota_func(c, a_val) - c
    
    # Szukamy rozwiązań numerycznie.
    # Wiemy, że 0 jest zawsze rozwiązaniem. Szukamy innych w zakresie 0.1 - 1.0
    guesses = [0, 0.3, 0.6, 0.8]
    roots = set()
    for g in guesses:
        root = fsolve(equation, g)[0]
        if root >= 0:
            roots.add(round(root, 5)) # zaokrąglamy by usunąć duplikaty
            
    sorted_roots = sorted(list(roots))
    
    for c_star in sorted_roots:
        deriv = derivative_lasota(c_star, a_val)
        stability = "STABILNY" if abs(deriv) < 1 else "NIESTABILNY"
        print(f"  Punkt stały c* = {c_star:.5f}, f'(c*) = {deriv:.4f} -> {stability}\n")

# Uruchomienie analizy
analyze_stability(0.2)
analyze_stability(0.3)