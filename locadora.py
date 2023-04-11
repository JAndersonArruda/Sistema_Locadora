import datetime

class Locadora:
  def __init__(self, lista_equipamentos, nome_locadora):
    self.lista_equipamentos = lista_equipamentos
    self.nome_locadora = nome_locadora
    self.equipamentos_D = {}

    with open(self.lista_equipamentos) as equipamento:
      conteudo = equipamento.readlines()
    id = 1001
    for i in conteudo:
      self.equipamentos_D.update({str(id):{"equipamento": i.replace('\n', ''), "nome_Empr": '', "data_Empr": '',"estado": 'desponivel'}})
      id = id + 1

  def imprimir(self):
    print("----------------lista de equipamentos-------------------")
    print("id equipamento", "\t", "título", "\t", "estado")
    print("--------------------------------------------------------")
    for chave, valor in self.equipamentos_D.items():
      print(f"{chave} \t\t {valor.get('equipamento')}\t [{valor.get('estado')}]")

  def emprestimo(self):
    id_Equipamento = input("informe o id do equipamento: ")
    data_Atual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if id_Equipamento in self.equipamentos_D.keys():
      if self.equipamentos_D[id_Equipamento]["estado"] == 'disponivel':
        nome = input("Informe seu nome: ")
        self.equipamentos_D[id_Equipamento]["nome_Empr"] = nome
        self.equipamentos_D[id_Equipamento]["data_Empr"] = data_Atual
        self.equipamentos_D[id_Equipamento]["estado"] = "não disponivel"
        print("Emprestimo realizado!")
      elif not (self.equipamentos_D[id_Equipamento]["estado"] == "disponivel"):
        print(f"Esse equipamento foi emprestado para {self.equipamentos_D[id_Equipamento]['nome_Empr']} em {self.equipamentos_D[id_Equipamento]['data_Empr']}")
      return self.emprestimo()
    else:
      print("Equipamento não encontrado!")
      return self.emprestimo()

  def adicionar(self):
    nome_Equipamento = input("Informe o nome do equipamento: ")
    if nome_Equipamento == '':
      return self.adicionar()
    elif len(nome_Equipamento) > 20:
      print("O nome do equipamento possui muitos caracteres, o limete é 20!")
      return self.adicionar()
    else:
      with open(self.lista_equipamentos, 'a') as equipamento:
        equipamento.writelines(f"{nome_Equipamento}\n")
        self.equipamentos_D.update({str(int(max(self.equipamentos_D))+ 1):{"equipamento": nome_Equipamento , "nome_Empr": '', "data_Empr": '',"estado": 'desponivel'}})
        print(f"O equipamento '{nome_Equipamento}' foi adicionado!")
  
  def devolucao(self):
    id_Equipamento = input("Informe o ID do equipamento: ")
    if id_Equipamento in self.equipamentos_D.keys():
      if self.equipamentos_D[id_Equipamento]['estado'] == "disponivel":
        print("Este equipamento não foi alugado, verifique o ID!")
        return self.devolucao()
      elif not (self.equipamentos_D[id_Equipamento]["estado"]) == "disponivel":
        self.equipamentos_D[id_Equipamento]["nome_Empr"] = ''
        self.equipamentos_D[id_Equipamento]["data_Empr"] = ''
        self.equipamentos_D[id_Equipamento]["estado"] = 'disponivel'
        print("Devolução realizada!")