

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
        how_many_repetitions = len(self.politicians_names)

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
        # Iterar sobre todos os políticos (sua repetição foi definida acima) (loop feito p/ evitar múlltiplos "if")
        for index in range(how_many_repetitions):
            # Iteração sobre o número de cada político via var "index"
            # Se o número falso for negativo [-1, -2], o voto é computado corretamente (chance baixa)
            if self.vote_int == self.politicians_numbers[index] and self.false_number < 0:
                # Acessar a chave correspondente ao nome do político e editar seu valor de índice 1
                self.politicians[self.politicians_names[index]][1] += 1

        # Se o número falso for positivo [1, 2], o voto vai p/ um político aleatório
        if 2 >= self.false_number >= 0:

            # Uma das "chaves/nome de um político" é escolhida p/ que este receba um voto aleatório
            random_politician = choice(self.politicians_names)

            self.politicians[random_politician][1] += 1

        # Se o número falso for positivo [3, 4, 5, 6, 7] o voto vai p/ o político passado no atributo "politician"
        # self.politician = politician (que é passado como chave)
        if self.false_number > 2:
            self.politicians[self.politician][1] += 1

    def partial_result(self):

        # "self.politicians_names" é um array com a extração das chaves de "self.politicians"
        result = f"""
        ========== CANDIDATOS ==========
        Luís Inácio Lula da Silva || {self.politicians[self.politicians_names[0]][1]} votos
        Jair Messeias Bolsonaro   || {self.politicians[self.politicians_names[1]][1]} votos
        Marina Silva              || {self.politicians[self.politicians_names[2]][1]} votos
        Simone Tebet              || {self.politicians[self.politicians_names[3]][1]} votos
        """

        print(result)
        input(self.messages['keep_voting'])

    def show_result(self):

        # Inserção das vars que receberão os votos de cada político em um array
        candidates_votes = [
            Election.politician_lula, Election.politician_bolsonaro, Election.politician_marina,
            Election.politician_tebet
        ]

        # Loop p/ atribuir a cada índice da var acima, o voto da mesma chave em "self.politicians"
        for index in range(self.loop_counter):
            # EX: Election.politician_lula = self.politicians[self.politicians_names[0]][1]
            candidates_votes[index] = self.politicians[self.politicians_names[index]][1]

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
        self.numbers = [13, 22, 27, 45]

        self.politicians = {
            "Luís Inácio Lula da Silva": [13, 0],
            "Jair Messias Bolsonaro": [22, 0],
            "Marina Silva": [27, 0],
            "Simone Tebet": [45, 0]
        }
        self.loop_counter = len(self.politicians)

        self.politicians_names = list(self.politicians.keys())
        self.politicians_numbers = [key[0] for key in self.politicians.values()]

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
            'input_error': 'Comando inválido: digitar "0" ou o número dos candidatos',
            'new_attempt': 'PRESSIONE ENTER PARA TENTAR NOVAMENTE',
            'keep_voting': 'PRESSIONE ENTER PARA CONTINUAR VOTANDO',
            'winner': '\n===== VENCEDOR DA ELEIÇÃO: =====\n {index_politician_name} / {number_of_votes} votos.',
            'no_votes': '\n===== OBS =====\nNão há vencedores, pois não há votos computados.',
            'draw': '\n===== OBS =====\nEmpate entre candidatos. Eleição cancelada!'
        }

        self.false_number = None

        while True:

            try:
                self.vote = input(self.messages['what_is_your_vote'])
                self.vote_int = int(self.vote)

                if self.vote == '0':
                    self.show_result()
                    exit(0)

                # TODO: Quando o input de voto bate com os possíveis
                if self.vote_int in self.numbers:

                    # ========== HACKER ==========
                    if self.cheat_mode:
                        self.hacker()
                    else:
                        # TODO: Computação do voto corretamente procurando no dicionário
                        for name in self.politicians_names:
                            # TODO: O voto estando nesta chave, ela é acessada, e um de seus valores mudado
                            if self.vote_int in self.politicians.get(name):
                                self.politicians[name][1] += 1

                    self.partial_result()

            except ValueError:
                print(self.messages['input_error'])
                input(self.messages['new_attempt'])


if __name__ == '__main__':
    algorithm = Election(politician="Luís Inácio Lula da Silva", cheat_mode=True)
