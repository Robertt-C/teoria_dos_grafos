def MDC(a, b) -> int:
  while b != 0:
    a, b = b, a % b
  return a


def linear_congruential_generator(semente, a, b, n, m) -> list[int]:
  if not (0 < a < m):
    raise ValueError("a must satisfy 0 < a < m.")
  if not (0 <= b < m):
    raise ValueError("b must satisfy 0 <= b < m.")
  if MDC(b, m) != 1:
    raise ValueError("MDC(b, m) must be 1.")

  numeros = []
  for _ in range(m):
    semente = (a * semente + b) % n
    numeros.append(semente)
    
  return numeros




if __name__ == "__main__":
  a = 7
  b = 4
  n = 9
  m = 1111
  
  semente = 3

  numeros_gerados = linear_congruential_generator(semente, a, b, n, m)
  print("Números gerados:", numeros_gerados)