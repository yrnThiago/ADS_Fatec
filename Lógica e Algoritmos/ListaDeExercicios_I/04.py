salary = float(input())
rise = salary * (float(input()) / 100)  

print(f"Aumento: R$ {rise:.2f}\nNovo salário: R$ {salary + rise:.2f}")