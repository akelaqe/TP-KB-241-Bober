def discriminant(a, b, c):
    return b**2 - 4*a*c

a, b, c = 1, 5, 6
D = discriminant(a, b, c)
print(f"Дискримінант для рівняння {a}x² + {b}x + {c} = 0 дорівнює {D}")