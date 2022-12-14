

from random import choice


class Election:

    # def show_result
    politician_ciro = 0
    politician_eymael = 0
    politician_felipe = 0
    politician_bolsonaro = 0
    politician_pericles = 0
    politician_lula = 0
    politician_kelmon = 0
    politician_tebet = 0
    politician_sofia = 0
    politician_soraya = 0
    politician_vera = 0

    absolute_freq = 0

    loop_counter = 0

    # Uso em: [def show_partial_result, def show_final_election_status]
    def show_current_election_status(self, show_votes=False):
        Election.absolute_freq = sum([key['votes'] for key in self.politicians])
        # for key in self.politicians:
        #     print(key['votes'])
        # print('----->', absolute_freq)

        if not show_votes:

            # Nome do político, porcentagem do político
            current_percentages = []
            for index, data in enumerate(self.numbers):
                # Nome do político, votos computados ao político, porcentagem dos votos do político
                current_percentages.append(
                    (
                        self.politicians[index]['politician'],
                        float((self.politicians[index]["votes"] * 100) / Election.absolute_freq)
                    )
                )

            # Organização dos dados pelo índice aninhado 1 do array acima (valor de porcentagem)
            sorted_current_percentages = sorted(current_percentages, key=lambda index_n: index_n[1], reverse=True)

            return sorted_current_percentages

        if show_votes:
            return Election.absolute_freq

    # Usado ao final do algoritmo
    def show_final_election_status(self):
        Election.absolute_freq = sum([key['votes'] for key in self.politicians])
        votes_so_far = self.show_current_election_status(show_votes=True)
        report = f'\n{self.p}========== RESULTADO =========='
        computed_votes = f"{self.p}{votes_so_far} votos computados"

        # [(Nome do político, votos computados ao político, porcentagem dos votos do político), ...]
        current_percentages = []
        for index, data in enumerate(self.numbers):
            current_percentages.append(
                (
                    self.politicians[index]['politician'],
                    self.politicians[index]['votes'],
                    float((self.politicians[index]["votes"] * 100) / Election.absolute_freq)
                )
            )

        # Organização das tuplas pelo índice aninhado 2 (porcentagem dos votos do político)
        sorted_current_percentages = sorted(current_percentages, key=lambda index_n: index_n[2], reverse=True)

        print(report)
        print(computed_votes)
        for tuple_ in sorted_current_percentages:
            politician_percentage = tuple_[2]
            politician_votes = tuple_[1]
            politician_name = tuple_[0]
            print(f"{self.p}[ {f'{politician_percentage:.2f}'}% ] [ {politician_votes} votos ] {politician_name}")

    # Função usada quando o parâmetro "cheat_mode=True"
    def hacker(self):

        # A var é modificada aqui. Se for feito direto em __init__, não funcionará (foi testado)
        self.false_number = choice([*range(-2, 11)])

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

        "VERSÃO REFATORADA [index = índice de cada político, para previnir múltiplos if]"
        # TODO: Voto certo (-1 ao -2)
        for index in range(n_repetitions):
            # Para computação correta, é preciso: número correto + número falso (-1 ao -2) (chance baixa)
            if self.vote_int == self.politicians_numbers[index] and self.false_number < 0:
                # Acessar a chave correspondente ao político e editar seu valor
                self.politicians[index]["votes"] += 1
                Election.loop_counter += 1

        # TODO: Voto aleatório (1 ao 9)
        if 0 <= self.false_number <= 9:
            random_politician_index = choice(self.random_politician_index)

            # Nome do político != parâmetro / Número do político != input "self.vote_int"
            if self.politicians[random_politician_index] != self.benefited \
               and self.politicians[random_politician_index]['id'] != self.vote_int:
                self.politicians[random_politician_index]["votes"] += 1
                Election.loop_counter += 1

        # TODO: Voto ao alvo beneficiado injustamente (10) (parâmetro "politician")
        if self.false_number > 9:
            # Achar o político via chave == parâmetro passado (candidato beneficiado pelo hacker)
            for index, data in enumerate(self.politicians):
                if data["politician"] == self.benefited:
                    self.politicians[index]["votes"] += 1
                    Election.loop_counter += 1

    "REMOVIDO"
    # def partial_result(self):
    #     votes_so_far = self.show_current_election_status(show_votes=True)
    #     election_panel = self.show_current_election_status()
    #     banner = f'{self.p}VOTOS COMPUTADOS: {votes_so_far} votos'
    #     label = f'{self.p}========== CANDIDATOS =========='
    #
    #     print(banner)
    #     print(label)
    #     for tuple_ in election_panel:
    #         politician_percentage = tuple_[1]
    #         politician_name = tuple_[0]
    #         print(f"{self.p}[ {f'{politician_percentage:.2f}'}% ] {politician_name}")
    #     print('\n')

    def show_result(self):
        # Inserção das vars que receberão os votos de cada político em um array
        candidates_votes = [
            Election.politician_ciro,
            Election.politician_eymael,
            Election.politician_felipe,
            Election.politician_bolsonaro,
            Election.politician_pericles,
            Election.politician_lula,
            Election.politician_kelmon,
            Election.politician_tebet,
            Election.politician_sofia,
            Election.politician_soraya,
            Election.politician_vera
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

            # Adquirir a porcentagem p/ exibir no print
            Election.absolute_freq = sum([key['votes'] for key in self.politicians])
            winner_percentage = f'[ {float((self.politicians[winner_index]["votes"] * 100) / Election.absolute_freq):.2f}% ]'

            # Mostrar o vencedor ("winner_index" acerta pois "len(self.politicians_names) == len(candidates_votes)")
            print(self.messages['winner'].format(
                indent=self.p,
                indent2=self.p,
                index_politician_name=self.politicians_names[winner_index],
                number_of_votes=winner,
                percentage=winner_percentage)
            )

        # Se há algum voto computado e se há empate (eleição cancelada)
        if winner > 0 and draw_happened[0]:
            print(self.messages['draw'])

        # Se não há algum voto computado
        if winner == 0:
            print(self.messages['no_votes'])

    def __init__(self, benefited, max_votes, cheat_mode: bool = False):
        self.benefited = benefited
        self.cheat_mode = cheat_mode

        "APENAS PARA ESSA VERSÃO DO ALGORITMO"
        self.max_votes = max_votes

        self.p = '        '

        self.politicians = [
            {"politician": "Ciro Gomes", "id": 12, "votes": 0},
            {"politician": "Eymael", "id": 27, "votes": 0},
            {"politician": "Felipe D'Avila", "id": 30, "votes": 0},
            {"politician": "Jair Messias Bolsonaro", "id": 22, "votes": 0},
            {"politician": "Leo Péricles", "id": 80, "votes": 0},
            {"politician": "Luís Inácio Lula da Silva", "id": 13, "votes": 0},
            {"politician": "Padre Kelmon", "id": 14, "votes": 0},
            {"politician": "Simone Tebet", "id": 15, "votes": 0},
            {"politician": "Sofia Manzano", "id": 21, "votes": 0},
            {"politician": "Soraya Thronicke", "id": 44, "votes": 0},
            {"politician": "Vera Lúcia", "id": 16, "votes": 0},
        ]

        # Controlar os inputs que o user pode inserir (list(range(11))
        self.numbers = [key['id'] for key in self.politicians]

        # Índices de "self.politicians". Essa var existe, pois os dados são JSON (array com dicionários)
        self.random_politician_index = [*range(len(self.politicians))]

        # def show_result
        self.loop_counter = len(self.politicians)

        self.politicians_names = [name['politician'] for name in self.politicians]
        self.politicians_numbers = [name['id'] for name in self.politicians]

        self.menu = f"""\n
        ENCERRAR ELEIÇÃO: digite 0

        ========== CANDIDATOS ==========
        12 || Ciro Gomes
        27 || Eymael
        30 || Felipe D'Avila
        22 || Jair Messias Bolsonaro
        80 || Leo Péricles
        13 || Luís Inácio Lula da Silva
        27 || Marina Silva
        14 || Padre Kelmon
        15 || Simone Tebet
        21 || Sofia Manzano
        44 || Soraya Thronicke
        16 || Vera Lúcia
        Digite após a seta -> """

        self.messages = {
            'what_is_your_vote': f'\n{self.p}{f"Qual o seu voto para presidente?".upper()} {self.menu}',
            'input_error': f'\n{self.p}Comando inválido: digitar "0" ou o número dos candidatos no MENU',
            'new_attempt': f'{self.p}PRESSIONE ENTER PARA TENTAR NOVAMENTE',
            'keep_voting': f'{self.p}PRESSIONE ENTER PARA CONTINUAR VOTANDO',
            'winner': '\n{indent}===== VENCEDOR =====\n{indent2}{index_politician_name} / {number_of_votes} votos / {percentage}',
            'no_votes': '\n===== AVISO =====\nNão há vencedores, pois não há votos computados.',
            'draw': f'\n{self.p}===== AVISO =====\n{self.p}Empate entre candidatos. Eleição cancelada!'
        }

        # "def hacker" (é provável que uma var de classe possa substituir isso)
        self.false_number = None

        # Adicionado por último, por estar gerando um erro que eu não sei como resolver (ver except abaixo)

        while Election.loop_counter < self.max_votes:

            "NESTA VERSÃO DO ALGORITMO, O INPUT É SUBSTITUÍDO POR UM VALOR FIXO"
            # Coletar o dado de voto do usuário
            self.vote_int = 12

            # O usuário fornece um número de candidato correto
            if self.vote_int in self.numbers:

                # ========== HACKER LIGADO ========== Voto computado (chance muita baixa de computação correta)
                if self.cheat_mode:
                    self.hacker()
                    # self.partial_result()

                # ========== HACKER DESLIGADO ========== Voto computado corretamente
                else:
                    # SUPOSIÇÕES [self.vote_int = 12] [self.politicians_numbers = [vários números]]
                    # "index" é o monitor do índice entre [self.vote_int] e [self.politicians_numbers]
                    # Em algum momento, o número [self.vote_int] acha o número em [self.politicians_numbers]
                    # Quando achar, é pelo "index" que o voto é computado corretamente
                    for index, number in enumerate(self.politicians_numbers):
                        if self.vote_int == number:
                            self.politicians[index]["votes"] += 1

                    # Exibe a contagem de votos atual
                    Election.loop_counter += 1
                    self.show_result()
                    self.show_final_election_status()

            # O usuário não fornece um número de candidato correto
            else:
                print(self.messages['input_error'])
                input(self.messages['new_attempt'])

            # O 'if' não é necessário, está aqui apenas como referência para saber onde acaba
            if Election.loop_counter >= self.max_votes:
                self.show_result()
                self.show_final_election_status()


if __name__ == '__main__':
    algorithm = Election(benefited="Luís Inácio Lula da Silva", max_votes=200_000, cheat_mode=True)
