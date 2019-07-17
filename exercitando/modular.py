from mod import Mod

# Matematica modular

modulo = 7 # [0, 1, 2, 3, 4, 5, 6, 7]

x = Mod(10, modulo)

print(x) # Resto da divisão com o modulo corresponde ao numero no universo modular

#print((x + 2) == 0)       # True: 5 + 2 ≡ 7 ≡ 0 (mod 7)
#print((x + 7) == x)      # True: 5 + 7 ≡ 12 ≡ 5 (mod 7)
#print((x**3) == (x + 1))  # True: 5³ ≡ 125 ≡ 6 (mod 7)
#print((1 //x) == 3)      # True: 5 × 3 ≡ 15 ≡ 1 (mod 7) ⇒ 5⁻¹ ≡ 3 (mod 7)

print(8 % modulo)