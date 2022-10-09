

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
        absolute_freq = sum([key['votes'] for key in self.politicians])

        if not show_votes:
            # Nome do político, porcentagem do político
            current_percentages = []
            for index, data in enumerate(self.politicians_numbers):
                # Nome do político, votos computados ao político, porcentagem dos votos do político
                current_percentages.append(
                    (
                        self.politicians[index]['politician'],
                        float((self.politicians[index]["votes"] * 100) / absolute_freq)
                    )
                )

            # Organização dos dados pelo índice aninhado 1 do array acima (valor de porcentagem)
            sorted_current_percentages = sorted(current_percentages, key=lambda index_n: index_n[1], reverse=True)

            return sorted_current_percentages

        if show_votes:
            return absolute_freq

    # Usado ao final do algoritmo
    def show_final_election_status(self):
        absolute_freq = sum([key['votes'] for key in self.politicians])
        report = f'\n{self.p}========== RESULTADO =========='
        computed_votes = f"{self.p}{self.show_current_election_status(show_votes=True)} votos computados"

        # [(Nome do político, votos computados ao político, porcentagem dos votos do político), ...]
        current_percentages = []
        for index, data in enumerate(self.politicians_numbers):
            current_percentages.append(
                (
                    self.politicians[index]['politician'],
                    self.politicians[index]['votes'],
                    float((self.politicians[index]["votes"] * 100) / absolute_freq)
                )
            )

        # Organização das tuplas pelo índice aninhado 2 (porcentagem dos votos do político)
        sorted_current_percentages = sorted(current_percentages, key=lambda index_n: index_n[2], reverse=True)

        print(report)
        print(computed_votes)
        # Porcentagem dos votos do político, votos computados ao político, nome do político (organizados)
        for tuple_ in sorted_current_percentages:
            print(f"{self.p}[ {f'{tuple_[2]:.2f}'}% ] [ {tuple_[1]} votos ] {tuple_[0]}")

    def ask_for_politician_number(self):
        try:
            # Coletar o dado de voto do usuário
            vote = int(input(self.messages['what_is_your_vote']))
            self.vote_int = vote
            return self.vote_int

        except ValueError:
            print(self.messages['wrong_vote_value'])
            input(f'{self.p}PRESSIONE ENTER PARA REINICIAR')
            # self.__init__(benefited="Luís Inácio Lula da Silva", cheat_mode=True)
            self.ask_for_politician_number()

    # Função usada quando o atributo "cheat_mode=True"
    def hacker(self):

        # A var é modificada aqui. Se for feito direto em __init__, não funcionará (foi testado)
        self.false_number = choice([*range(-2, 13)])

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
        # TODO: Voto certo (-1 ao -2)
        for index in range(n_repetitions):
            # Para computação correta, é preciso: número correto + número falso (-1 ao -2) (chance baixa)
            if self.vote_int == self.politicians_numbers[index] and self.false_number < 0:
                # Acessar a chave correspondente ao político e editar seu valor
                self.politicians[index]["votes"] += 1
                Election.loop_counter += 1

        # TODO: Voto aleatório (1 ao 7)
        if 0 <= self.false_number <= 7:
            random_politician_index = choice(self.random_politician_index)

            # Nome do político != parâmetro / Número do político != input "self.vote_int"
            if self.politicians[random_politician_index] != self.benefited \
                    and self.politicians[random_politician_index]['id'] != self.vote_int:
                self.politicians[random_politician_index]["votes"] += 1
                Election.loop_counter += 1

        # TODO: Voto ao alvo beneficiado injustamente (7 ao 12) (parâmetro "politician")
        if self.false_number > 7:
            # Achar o político via chave == parâmetro passado (candidato beneficiado pelo hacker)
            for index, data in enumerate(self.politicians):
                if data["politician"] == self.benefited:
                    self.politicians[index]["votes"] += 1
                    Election.loop_counter += 1

    def partial_result(self):

        banner = f'\n{self.p}VOTOS COMPUTADOS: {self.show_current_election_status(show_votes=True)} votos'

        print(banner)
        print(f'{self.p}========== CANDIDATOS ==========')
        for tuple_ in self.show_current_election_status():
            # Porcentagem do candidato e nome do candidato
            print(f"{self.p}[ {f'{tuple_[1]:.2f}'}% ] {tuple_[0]}")

        "REMOVIDO NESTE ALGORITMO PARA QUE O LOOP FUNCIONE LIVREMENTE"
        # input(self.messages['keep_voting'])

        input(self.messages['keep_voting'])

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
            absolute_freq = sum([key['votes'] for key in self.politicians])
            winner_percentage = f'[ {float((self.politicians[winner_index]["votes"] * 100) / absolute_freq):.2f}% ]'

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
            exit(0)

        # Se não há algum voto computado
        if winner == 0:
            print(self.messages['no_votes'])
            exit(0)

    def __init__(self, benefited, cheat_mode: bool = False):
        """
        -> Cada chave self.politicians['politician']
        self.politicians_names = [
            'Ciro Gomes', 'Eymael', "Felipe D'Avila", 'Jair Messias Bolsonaro', 'Leo Péricles',
            'Luís Inácio Lula da Silva', 'Padre Kelmon', 'Simone Tebet', 'Sofia Manzano', 'Soraya Thronicke',
            'Vera Lúcia'
        ]

        -> Cada chave self.politicians['id']
        self.politicians_numbers = [12, 27, 30, 22, 80, 13, 14, 15, 21, 44, 16]

        -> Índices de self.politicians
        self.random_politician_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        -> Tamanho de um dado diretamente relacionado com "self.politicians" (Todos acima têm len() = 11)
        self.loop_counter = 11

        ================================ TUTORIAL: Como usar var de input em uma classe ================================
        . A "var self" que representa o input é instanciada sem valor definido, antes de qualquer loop (self.vote_int)
        . Se cria uma função própria para o lançamento do input (ask_for_politician_number)
        . Na função do input, uma "var comum" é lançada como input, para depois a "var self" do input receber seu valor
        . Na função do input, a "var self" é retornada, e se necessário, ter um tratamento "try" & "except"
        . Se há tratamento, é preciso que a função seja chamada dentro dela mesma
        . O input principal, para funcionar corretamente, deve vir inicialmente, fora do loop
        . O input principal é lançado em formato de função, sem instanciar uma var, pois a var já existe na função
        . O input principal neste algoritmo é "self.ask_for_politician_number()"
        . A cada situação de definição e erro, o input principal é relançado (self.ask_for_politician_number())
        . Se for pesquisado no arquivo do algoritmo "self.ask_for_politician_number", temos cada situação de seu uso

        ONDE O INPUT FOI USADO?
            . No início do algoritmo
            . Após mostrar o resultado parcial (quando hacker estiver ligado)
            . Após mostrar o resultado parcial (quando hacker não estiver ligado)
            . Após o usuário fornecer dados errados (número de político inexistente)
            . Na própria função do input quando o usuário fornecer dados não numéricos
            . Quando há empate

        ================================================== PROBLEMAS ==================================================
        . Existe algum erro acontecendo na função "partial_result", em seu loop for
        . O problema parece acontecer em "Election.absolute_freq"
        . "Election.absolute_freq" é usada diretamente em "self.show_current_election_status", que usa "partial_result"
        . "Election.absolute_freq", está sendo definida, em alguns casos menos recorrentes, como 0
        . Consequência? gera erro "ZeroDivisionError", pois "Election.absolute_freq" é um divisor
        . SOLUÇÃO: Tratar o erro, reenviando o input principal (talvez criar uma mensagem customizada)
        """

        self.benefited = benefited
        self.cheat_mode = cheat_mode
        self.p = '        '

        # Array matriz, nomes dos políticos do array, número dos políticos do array, índices do array, tamanho ao array
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
        self.politicians_names = [name['politician'] for name in self.politicians]
        self.politicians_numbers = [name['id'] for name in self.politicians]
        self.random_politician_index = [*range(len(self.politicians))]
        self.loop_counter = len(self.politicians)

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

        # Tratamentos e informações
        self.messages = {
            'what_is_your_vote': f'\n{self.p}{f"Qual o seu voto para presidente?".upper()} {self.menu}',
            'input_error': f'\n{self.p}Comando inválido: digitar "0" ou o número dos candidatos no MENU',
            'new_attempt': f'{self.p}PRESSIONE ENTER PARA TENTAR NOVAMENTE',
            'keep_voting': f'{self.p}PRESSIONE ENTER PARA CONTINUAR VOTANDO',
            'winner': '\n{indent}===== VENCEDOR =====\n{indent2}{index_politician_name} / {number_of_votes} votos / {percentage}',
            'no_votes': f'\n{self.p}===== ERRO =====\n{self.p}Não há vencedores, pois não há votos computados.',
            'draw': '\n===== ERRO =====\nEmpate entre candidatos. Eleição cancelada!',
            'wrong_vote_value': f'\n{self.p}========== ERRO ==========\n{self.p}Apenas números dos candidatos são permitidos'
        }

        # "def hacker" (é provável que uma var de classe possa substituir isso)
        self.false_number = None

        self.vote_int = None

        try:

            # O input principal, para funcionar corretamente, deve vir inicialmente, fora do loop
            self.ask_for_politician_number()

            while True:

                # Encerrar algoritmo
                if self.vote_int == 0:
                    self.show_result()
                    self.show_final_election_status()
                    exit(0)

                # O usuário fornece um número de candidato correto
                if self.vote_int in self.politicians_numbers:

                    # ========== HACKER LIGADO ========== Voto computado (chance muita baixa de computação correta)
                    if self.cheat_mode:
                        self.hacker()
                        self.partial_result()
                        self.ask_for_politician_number()

                    # ========== HACKER DESLIGADO ========== Voto computado corretamente
                    else:
                        # "index" acessa o índice do candidato certo
                        # "number" compara o voto passado por input com o número dos políticos
                        for index, number in enumerate(self.politicians_numbers):
                            if self.vote_int == number:
                                self.politicians[index]["votes"] += 1

                        # Exibe a contagem de votos atual
                        self.partial_result()
                        self.ask_for_politician_number()

                # TRATAMENTO: O usuário não fornece um número de candidato correto
                else:
                    print(self.messages['input_error'])
                    input(self.messages['new_attempt'])
                    self.ask_for_politician_number()

        except ZeroDivisionError:
            self.__init__(benefited="Luís Inácio Lula da Silva", cheat_mode=True)


if __name__ == '__main__':
    algorithm = Election(benefited="Luís Inácio Lula da Silva", cheat_mode=True)
