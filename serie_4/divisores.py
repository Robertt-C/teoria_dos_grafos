# divisors dos números de 1 até 500

import matplotlib.pyplot as plt

def find_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)
  return divisors

num_divisors = {}
all_divisors = {}

for number in range(1, 501):
    divisors = find_divisors(number)
    all_divisors[number] = divisors
    num_divisors[number] = len(divisors)


plt.figure(figsize=(12, 6))
plt.scatter(
  list(num_divisors.keys()),
  list(num_divisors.values()),
  color='blue',
  s=10
)
plt.title('Quantidade de divisors de Números de 1 a 500')
plt.xlabel('Número')
plt.ylabel('Quantidade de divisors')
plt.grid(True)
plt.show()
