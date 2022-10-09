# simulador_eleicao_2022
Simular como um algoritmo pode fraudar eleições

algorithm.py
  . Algoritmo que usa dicionário p/ lidar com os dados (simplificado)

algorithm_v2.py
  . Algoritmo que usa array JSON p/ lidar com os dados (simplificado)

algorithm_v3.py
  . Algoritmo que usa array JSON p/ lidar com os dados (melhorado)

algorithm_v4.py 
  . Algoritmo para simular sua execução uma certa quantidade de vezes, para verificar como é feita 
    a distribuição de votos (se vão de fato em sua maioria para o beneficiado). A repetição se dá pelo
    parâmetro "max_votes". Em "self.vote_int", se testa o número do candidato que se deseja computar
    todos os votos definidos em "max_votes", que são roubados e dados para o político definido no
    parâmetro "benefited".

algorithm_v4.py (resultado de uma execução simulando 1.000.000 votos seguidos para Ciro Gomes)
    
    ===== VENCEDOR =====
    Luís Inácio Lula da Silva / 276701 votos / [ 27.67% ]

    ========== RESULTADO ==========
    1000000 votos computados
    [ 27.67% ] [ 276701 votos ] Luís Inácio Lula da Silva
    [ 14.17% ] [ 141671 votos ] Ciro Gomes
    [ 6.50% ] [ 65040 votos ] Padre Kelmon
    [ 6.48% ] [ 64801 votos ] Soraya Thronicke
    [ 6.47% ] [ 64695 votos ] Jair Messias Bolsonaro
    [ 6.46% ] [ 64632 votos ] Leo Péricles
    [ 6.46% ] [ 64575 votos ] Vera Lúcia
    [ 6.45% ] [ 64531 votos ] Sofia Manzano
    [ 6.45% ] [ 64479 votos ] Felipe D'Avila
    [ 6.45% ] [ 64463 votos ] Simone Tebet
    [ 6.44% ] [ 64412 votos ] Eymael