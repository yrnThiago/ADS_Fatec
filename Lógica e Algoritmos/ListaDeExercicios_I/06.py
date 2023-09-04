hours, min = f"{float(input()) / float(input()):.2f}".split(".")
hours = f"{hours}h" if (int(hours)) else ""
min = f"{min}min" if (int(min)) else ""

print(f"Tempo médio da viagem: {hours}{min}")