numeri = [1, 2, 3, 4, 5, 6]
somma = 0
for n in numeri:
    if n % 2 == 0:
        somma += n
    else:
        somma -=n
print(somma) 