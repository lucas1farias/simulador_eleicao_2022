

from random import choice


class Election:

    politician_bolsonaro = 0
    politician_lula = 0
    politician_tebet = 0
    politician_marina = 0

    # Função usada quando o atributo "cheat_mode=True"
    def hacker(self):

        # A var é modificada aqui. Se for feito direto em __init__, não funcionará (foi testado)
        self.false_number = choice([*range(-2, 8)])

        # Quantas vezes o loop abaixo será executado
        n_repetitions = len(self.politicians_names)

        "VERSÃO MENOS REFATORADA DO QUE ESTÁ ACONTECENDO NO LOOP"
        # if self.vote_int == 13 and self.false_number < 0:
        #     self.politicians["Luís Inácio Lula da Silva"][1] += 1
        # if self.vote_int == 22 and self.false_number < 0:
        #     self.politicians["Jair Messias Bolsonaro"][1] += 1
        # if self.vote_int == 27 and self.false_number < 0:
        #     self.politicians["Marina Silva"][1] += 1
        # if self.vote_int == 45 and self.false_number < 0:
        #     self.politicians["Simone Tebet"][1] += 1

        "VERSÃO REFATORADA"
        # Iteração no número de cada político via "index" (repetição definida acima) (esse loop evita múlltiplos "if")
        for index in range(n_repetitions):
            # Para computação correta, é preciso: número correto + número falso [-1, -2] (chance baixa)
            if self.vote_int == self.politicians_numbers[index] and self.false_number < 0:
                # Acessar a chave correspondente ao político e editar seu valor
                self.politicians[index]["votes"] += 1

        # Se o número falso for positivo [1, 2], o voto vai p/ um político aleatório
        if 2 >= self.false_number >= 0:

            # Escolha de um dos índices + [uso do índice] + escolha da chave a ser alterada
            random_politician_index = choice(self.random_politician_index)
            self.politicians[random_politician_index]["votes"] += 1

        # Se o número falso for positivo [3, 4, 5, 6, 7] o voto vai p/ o político passado no atributo "politician"
        if self.false_number > 2:
            # Achar o político via chave == parâmetro passado (candidato beneficiado pelo hacker)
            for index, data in enumerate(self.politicians):
                if data["politician"] == self.politician:
                    self.politicians[index]["votes"] += 1

    def partial_result(self):

        # "self.politicians" é um array JSON, onde os dicionários são todos com chaves iguais e acessáveis via índice
        result = f"""
        ========== CANDIDATOS ==========
        Luís Inácio Lula da Silva || {self.politicians[0]["votes"]} votos
        Jair Messeias Bolsonaro   || {self.politicians[1]["votes"]} votos
        Marina Silva              || {self.politicians[2]["votes"]} votos
        Simone Tebet              || {self.politicians[3]["votes"]} votos
        """

        print(result)
        input(self.messages['keep_voting'])

    def show_result(self):

        # Inserção das vars que receberão os votos de cada político em um array
        candidates_votes = [
            Election.politician_lula, Election.politician_bolsonaro, Election.politician_marina,
            Election.politician_tebet
        ]

        # Loop p/ atribuir a cada índice da var acima, o voto do mesmo índice em "self.politicians"
        for index in range(self.loop_counter):
            # EX: Election.politician_lula = self.politicians[0]["votes"]
            candidates_votes[index] = self.politicians[index]["votes"]

        # Maior valor neste array (qtd. de votos do político + votado)
        winner = max(candidates_votes)

        # Pegar o índice do maior valor (maior qtd. de votos) p/ ter acesso ao nome do vencedor, na primeiro condição
        winner_index = candidates_votes.index(winner)

        # Verificar se o maior valor está repetido no array de votos (o que indica empate)
        draw_happened = [True if candidates_votes.count(winner) > 1 else False]

        # Se há algum voto computado e se não há empate
        if winner > 0 and not draw_happened[0]:

            # Mostrar o vencedor
            # "winner_index" acerta o nome pois "len(self.politicians_names) == len(candidates_votes)"
            print(self.messages['winner'].format(
                index_politician_name=self.politicians_names[winner_index],
                number_of_votes=winner))

        # Se há algum voto computado e se há empate (eleição cancelada)
        if winner > 0 and draw_happened[0]:
            print(self.messages['draw'])

        # Se não há algum voto computado
        if winner == 0:
            print(self.messages['no_votes'])

    def __init__(self, politician, cheat_mode: bool = False):
        self.politician = politician
        self.cheat_mode = cheat_mode

        # Controlar os inputs que o user pode inserir
        self.numbers = [13, 22, 27, 45]

        self.politicians = [
            {"politician": "Luís Inácio Lula da Silva", "id": 13, "votes": 0},
            {"politician": "Jair Messias Bolsonaro", "id": 22, "votes": 0},
            {"politician": "Marina Silva", "id": 27, "votes": 0},
            {"politician": "Simone Tebet", "id": 45, "votes": 0}
        ]

        # Índices de "self.politicians". Essa var existe, pois os dados são JSON (array com dicionários)
        self.random_politician_index = [*range(len(self.politicians))]

        self.loop_counter = len(self.politicians)

        self.politicians_names = [name['politician'] for name in self.politicians]
        self.politicians_numbers = [name['id'] for name in self.politicians]

        self.menu = """\n
        ENCERRAR ELEIÇÃO: digite 0

        ========== CANDIDATOS ==========
        Luís Inácio Lula da Silva || 13
        Jair Messeias Bolsonaro   || 22
        Marina Silva              || 27
        Simone Tebet              || 45
        Digite após a seta -> """

        self.messages = {
            'what_is_your_vote': f'Qual o seu voto? {self.menu}',
            'input_error': 'Comando inválido: digitar "0" ou o número dos candidatos no MENU',
            'new_attempt': 'PRESSIONE ENTER PARA TENTAR NOVAMENTE',
            'keep_voting': 'PRESSIONE ENTER PARA CONTINUAR VOTANDO',
            'winner': '\n===== VENCEDOR DA ELEIÇÃO: =====\n {index_politician_name} / {number_of_votes} votos.',
            'no_votes': '\n===== OBS =====\nNão há vencedores, pois não há votos computados.',
            'draw': '\n===== OBS =====\nEmpate entre candidatos. Eleição cancelada!'
        }

        # Var usada na função "hacker". Seu valor só é definido na função, caso contrário, não funcionará
        self.false_number = None

        while True:

            # Coletar o dado de voto do usuário
            self.vote = input(self.messages['what_is_your_vote'])
            self.vote_int = int(self.vote)

            # Encerrar algoritmo
            if self.vote == '0':
                self.show_result()
                exit(0)

            # O usuário fornece um número de candidato correto
            if self.vote_int in self.numbers:

                # ========== HACKER LIGADO ========== Voto computado (chance muita baixa de computação correta)
                if self.cheat_mode:
                    self.hacker()
                    self.partial_result()

                # ========== HACKER DESLIGADO ========== Voto computado corretamente
                else:
                    # "index" acessa o índice do candidato certo
                    # "number" compara o voto passado por input com o número dos políticos
                    for index, number in enumerate(self.politicians_numbers):
                        if self.vote_int == number:
                            self.politicians[index]["votes"] += 1

                    # Exibe a contagem de votos atual
                    self.partial_result()

            # O usuário não fornece um número de candidato correto
            else:
                print(self.messages['input_error'])
                input(self.messages['new_attempt'])


if __name__ == '__main__':
    algorithm = Election(politician="Luís Inácio Lula da Silva", cheat_mode=True)
