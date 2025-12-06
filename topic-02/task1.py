def discriminant(a, b, c):
    return b**2 - 4*a*c

def quadratic_roots(a, b, c):
    D = discriminant(a, b, c)
    print(f"Дискримінант: {D}")

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return f"Рівняння має два корені: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2*a)
        return f"Рівняння має один корінь: x = {x}"
    else:
        return "Рівняння не має дійсних коренів."

print(quadratic_roots(1, 5, 6))