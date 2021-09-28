segundos = int(input(""))
h = segundos // 3600
resto = segundos % 3600
m = resto // 60
s = resto % 60
print(f"{h}:{m}:{s}")
