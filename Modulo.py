verdier = []
modulo_value = 42
for i in range(10):
    verdier.append(int(input()))
unike_verdier = []
for i in verdier:
    if  i % modulo_value not in unike_verdier:
        unike_verdier.append(i % modulo_value)

print(len(unike_verdier))
