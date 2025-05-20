# Número de placas (NCD-4000 até NCD 9999) que possuem os dígitos todos diferentes

def has_all_unique_digits(n):
  s = str(n)
  return len(set(s)) == len(s)

count = 0

for plate_number in range(4000, 10000):
  if has_all_unique_digits(plate_number):
    count += 1

print(f"Número de placas com todos os dígitos diferentes: {count}")