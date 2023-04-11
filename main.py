from locadora import Locadora as L

try:
  l1 = L("equipamentos.txt", "Leo Costruções")
  menu = {'L': "Listar", 'A': "Alugar", 'E': "Encerir", 'D': "Devolução", 'S': "Sair"}
    
  op = False
  while not(op == 's'):
      print(f"\n-----------------{l1.nome_locadora}---------------------\n")
      for chave, valor in menu.items():
        print(chave, ": ", valor)
        
      op = input("opção: ").lower()

      if op == 'l':
        print("\n Opção: Listar\n")
        l1.imprimir()
      
      elif op == 'a':
        print("\n Opção: Alugar\n")
        l1.emprestimo()
      
      elif op == 'e':
        print("\n Opção: Encerir\n")
        l1.adicionar()
      
      elif op == 'd':
        print("\n Opção: Devolução\n")
        l1.devolucao()
      
      elif op == 's':
        break

      else:
        continue

except Exception as e:
  print("Algo deu errado!")
  print(str(e))