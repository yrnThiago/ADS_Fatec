days = int(input()) * 24 * 60 ** 2
hours = int(input()) * 60 ** 2
min = int(input()) * 60
sec = int(input())

print(f"Total: {days + hours + min + sec}s")