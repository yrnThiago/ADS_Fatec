def eh_primo(num: int) -> bool:
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
        
    return True

print(eh_primo(int(input())))