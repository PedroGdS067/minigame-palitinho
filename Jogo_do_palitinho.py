import os

class Jogador:
    # Projeto Jogo do Palitinho
    def __init__ (self, nome: str, palitos: int, posicao: int):
        self.nome = nome
        self.palitos = palitos
        self.posicao = posicao
        print(f'Usuário {self.posicao} criado. {self.nome} tem {self.palitos} palitos')

    # Função para jogar a rodada
    def turno(self):
        mao = -1
        while mao > self.palitos or mao < 0:
            try:
                mao = int(input(f'{self.nome} você tem {self.palitos} palitos. Digite o número de palitos para jogar a rodada: '))
            except:
                mao = int(input(f'Valor inválido! {self.nome} você tem {self.palitos} palitos. Digite o número de palitos para jogar a rodada: '))
            if mao > self.palitos or mao <0:
                    print(f'Esse valor é inválido, você só tem {self.palitos} palitos.')
        return mao

    # Função para armazenar o palpite de cada jogador
    def palpite(self, blocks):
        try:
            palpites = int(input(f'{self.nome} palpite o número de palitos totais da jogada: '))
        except:
            palpites = int(input(f'Valor inválido! {self.nome} palpite o número de palitos totais da jogada: '))
        # Verificação se o palpite é valido
        while palpites in blocks:
            try:
                palpites = int(input(f'Um jogador já palpitou esse valor. {self.nome} palpite outro valor: '))
            except:
                palpites = int(input(f'Valor inválido! {self.nome} palpite o número de palitos totais da jogada: '))
        return palpites

    # Função para verificar se o jogador acertou o número de palitos
    def acertou(self):
        if self.palitos > 1:
            self.palitos -= 1
            print(f'{self.nome} acertou. Agora {self.nome} tem {self.palitos} palitos')
            play = True
        else:
            print(f'{self.nome} acertou!\nParabéns {self.nome}!! Você venceu!')
            play = False
        return play

class Partida:
    def __init__(self):
        self.quan = 0
        self.jog = []
        self.lista = []
        self.ordem = []
        self.p_iniciais = 0

    # Função para definir a quantidade de jogadores e palitos iniciais
    def quant_jog(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            self.quan = int(input("Digite a quantidade de jogadores: "))
        except:
            self.quan = int(input("Valor inválido. Digite a quantidade de jogadores: "))
        try:
            self.p_iniciais = int(input("Digite a quantidade de palitos iniciais dos jogadores: "))
        except:
            self.p_iniciais = int(input("Valor inválido. Digite a quantidade de palitos iniciais dos jogadores: "))
        return self.quan, self.p_iniciais

    # Função para criar os jogadores
    def cria(self):
        self.jog = []
        self.ordem = []
        for i in range(self.quan):
            nom = str(input(f'Digite o nome do jogador {i+1}: '))
            self.ordem.append(i)
            self.jog.append(i)
            self.jog[i] = Jogador(nome = nom, palitos = self.p_iniciais, posicao = i+1)
        return self.jog

    # Função para iniciar o jogo
    def jogar(self):
        rodada = 1
        play = True
        while play:
            os.system('cls' if os.name == 'nt' else 'clear')
            gabarito = -1
            total = 0
            lista_de_palpites = []
            self.lista = []
            # Ordenação dos jogadores
            for i in self.ordem:
                print(f'\nRodada {rodada}')
                aposta = self.jog[i].turno()
                total += aposta
                lista_aux = [self.jog[i].nome, self.jog[i].palitos]
                self.lista.append(lista_aux)
                os.system('cls' if os.name == 'nt' else 'clear')

            print(f'\nLista de jogadores e palitos totais restantes: {self.lista}')
            # Verificação e armazenamento dos palpites
            for i in self.ordem:
                chute = int(self.jog[i].palpite(lista_de_palpites))
                lista_de_palpites.append(chute)
                if chute == total:
                    gabarito=i

            print(f'\n')
            print(f'O número total de palitos jogados na rodada {rodada} foi {total}.')
            # Verificação se o jogador acertou o número de palitos
            if gabarito == -1:
                print(f'Ninguém acertou.')
            else:
                play = self.jog[gabarito].acertou()
            if play:
                input("Pressione enter para próximo turno")
            self.ordem.append(self.ordem[0])
            self.ordem.pop(0)
            rodada += 1

# Main
jogo = Partida()
jogo.quant_jog()
jogo.cria()
jogo.jogar()

