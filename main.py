
fila_bugs = []

def append(descricao, tempo):
  fila_bugs.append({"descricao": descricao, "tempo": tempo})

def input_int():
  return int(input())

def imprimir_operacoes():
  if not fila_bugs:
    print("Fila vazia")
  else:
    for index in fila_bugs:
      print(f"{index['descricao']} {index['tempo']}")

def cadastrar_bugs():
  descricao = input()
  tempo_estimado = input_int()
  append(descricao, tempo_estimado)

def atualizar_bugs():
  T = input_int()
  if not fila_bugs:
    print("Nao existem bugs cadastrados.")
    return
  elemento = fila_bugs[0]
  descricao, tempo_estimado = elemento["descricao"], elemento["tempo"] 
  del fila_bugs[0]
  tempo_atualizado = tempo_estimado - T
  if tempo_atualizado > 0:
    append(descricao, tempo_atualizado)


def main():
  qtd_op = input_int()
  if qtd_op < 1 or qtd_op > 100:
    print("Quantidade de operações inválida") 
  else:  
    for iter in range(qtd_op):
      cmd = input_int()
      if cmd == 0:
        cadastrar_bugs()
      elif cmd == 1:
        atualizar_bugs()
      else:
        continue
    imprimir_operacoes()

main()