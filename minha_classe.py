class ControleRemoto:
    
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
        
    def avancar_canal(self):
        print('Canal avancado')
        
    def voltar_canal(self):
        print('Voltar canal')
        
    def escolher_canal(self, canal):
        print('Alterado para o canal:  {}'.format(canal))
        

controle_sala = ControleRemoto('sansung', 'sala')
print(f'Comodo: {controle_sala.comodo}')
print(f'TV: {controle_sala.televisao}')
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)