product_price = float(input())
discount = product_price * (float(input()) / 100)  

print(f"Desconto: R$ {discount:.2f}\nNovo valor de produto: R$ {product_price - discount:.2f}")