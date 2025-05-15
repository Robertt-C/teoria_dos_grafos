def MDC(a, b) -> int:
  while b != 0:
    a, b = b, a % b
  return a


def linear_congruential_generator(semente, a, b, n, m) -> list[int]:
  if not (0 < a < m):
    raise ValueError("a deve satisfazer 0 < a < m.")
  if not (0 <= b < m):
    raise ValueError("b deve satsifazer 0 <= b < m.")
  if MDC(b, m) != 1:
    raise ValueError("MDC(b, m) deve ser igual a 1.")

  numeros = []
  for _ in range(m):
    semente = (a * semente + b) % n
    numeros.append(semente)
    
  return numeros




if __name__ == "__main__":
  a = 7
  b = 4
  n = 9
  m = 111
  semente = 3

  numeros_gerados = linear_congruential_generator(semente, a, b, n, m)
  print(numeros_gerados)