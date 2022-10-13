

# simulador_eleicao_2022 (Português)
Simular um algoritmo que pode aplicar eleições fraudulentas

<h4>Versões do algoritmo</h4>
<ol>
  <li><b>algorithm.py</b> é uma versão do algoritmo que use um dicionário para lidar com os dados (simplificado)</li>
  <li><b>algorithm_v2.py</b> é uma versão do algoritmo que usa um array JSON para lidar com os dados (simplificado)</li>
  <li><b>launcher.py</b> é uma versão melhorada de <b>algorithm_v2.py</b> e é o <b>algoritmo principal</b></li>
  <li><b>tester.py</b> é a versão de <b>launcher.py</b> sem o loop</li>
  <li><b>tester.py</b> é projetada para testar uma certa quantidade de votos e ver se eles se comportam da maneira esperada</li>
  <li><b>COMPORTAMENTO:</b> o número do político é configurado em <b>self.vote_int</b> em teoria, deve receber todos os votos configurados em <b>self.max_votes</b>, mas a distribuição de votos é esperada ser roubada em sua maioria para o parâmetro <b>benefited</b></li>
</ol>

# simulador_eleicao_2022 (English)
Simulate an algorithm that can apply cheatable elections

<h4>Versions of the algorithm</h4>
<ol>
  <li><b>algorithm.py</b> is a version of the algorithm which uses a dictionary to deal with the data (simplified)</li>
  <li><b>algorithm_v2.py</b> is a version of the algorithm which uses a JSON array to deal with the data (simplified)</li>
  <li><b>launcher.py</b> is an improved version of <b>algorithm_v2.py</b> and is the <b>main algorithm</b></li>
  <li><b>tester.py</b> is a version of <b>launcher.py</b> without the loop</li>
  <li><b>tester.py</b> is designed to test certain amount of votes and see if they behave as expected</li>
  <li><b>BEHAVIOR:</b> the number of the politician set in <b>self.vote_int</b> in theory, must receive all the votes set in <b>self.max_votes</b>, but the distribution of votes is expected to be stolen mostly to the parameter <b>benefited</b></li>
</ol>

<h4>Resultado / Result</h4>
<p>Resultado de uma execução simulando 1.000.000 votos seguidos para Ciro Gomes</p>
<p>Result of a running simulating 1.000.000 votes in a row for the politician Ciro Gomes</p>

###### ===== VENCEDOR =====
###### Luís Inácio Lula da Silva / 276701 votos / [ 27.67% ]

###### ========== RESULTADO ==========
###### 1000000 votos computados
###### [ 27.67% ] [ 276701 votos ] Luís Inácio Lula da Silva
###### [ 14.17% ] [ 141671 votos ] Ciro Gomes
###### [ 6.50% ] [ 65040 votos ] Padre Kelmon
###### [ 6.48% ] [ 64801 votos ] Soraya Thronicke
###### [ 6.47% ] [ 64695 votos ] Jair Messias Bolsonaro
###### [ 6.46% ] [ 64632 votos ] Leo Péricles
###### [ 6.46% ] [ 64575 votos ] Vera Lúcia
###### [ 6.45% ] [ 64531 votos ] Sofia Manzano
###### [ 6.45% ] [ 64479 votos ] Felipe D'Avila
###### [ 6.45% ] [ 64463 votos ] Simone Tebet
###### [ 6.44% ] [ 64412 votos ] Eymael
