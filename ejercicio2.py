def bleatrix_trotter(N):
    if N == 0:
        return "INSOMNIA"
    
    seen_digits = set()
    i = 0
    
    while len(seen_digits) < 10:
        i += 1
        seen_digits.update(str(i * N))  # Añade los digitos al conjunto
    
    return i * N

# Casos de prueba
print(f"Caso #1: {bleatrix_trotter(0)}")    # INSOMNIA
print(f"Caso #2: {bleatrix_trotter(1)}")    # 10
print(f"Caso #3: {bleatrix_trotter(1692)}") # 5076
