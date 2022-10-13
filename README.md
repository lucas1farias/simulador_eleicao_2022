

# simulador_eleicao_2022 (Português)
Simular um algoritmo que pode aplicar eleições fraudulentas

<h4>Versões do algoritmo</h4>
<ol>
  <li><b>algorithm.py</b> é uma versão do algoritmo que use um dicionário para lidar com os dados (simplificado)</li>
  <li><b>algorithm_v2.py</b> é uma versão do algoritmo que usa um array JSON para lidar com os dados (simplificado)</li>
  <li><b>launcher.py</b> é uma versão melhorada de <b>algorithm_v2.py</b> e é o <b>algoritmo principal</b></li>
  <li><b>tester.py</b> é a versão de <b>launcher.py</b> sem o loop</li>
  <li><b>tester.py</b> é projetada para testar uma certa quantidade de votos e ver se eles se comportam da maneira esperada</li>
  <li><b>COMPORTAMENTO:</b> o número do político é configurado em <b>self.vote_int</b> em teoria, deve receber todos os votos configurados em <b>self.max_votes</b>, mas a distribuição de votos é esperada ser roubada para o parâmetro <b>benefited</b></li>
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
  <li><b>BEHAVIOR:</b> the number of the politician set in <b>self.vote_int</b> in theory, must receive all the votes set in <b>self.max_votes</b>, but the distribution of votes is expected to be stolen to the parameter <b>benefited</b></li>
</ol>

<h4>Resultado / Result</h4>
<p>Resultado de uma execução simulando 200.000 votos seguidos para Ciro Gomes</p>
<p>Result of a running simulating 200.000 votes in a row for the politician Ciro Gomes</p>

###### ===== VENCEDOR =====
###### Ciro Gomes / 33092 votos / [ 16.55% ]

###### ========== RESULTADO ==========
###### 200000 votos computados
###### [ 16.55% ] [ 33092 votos ] Ciro Gomes
###### [ 15.96% ] [ 31926 votos ] Luís Inácio Lula da Silva
###### [ 7.64% ] [ 15283 votos ] Sofia Manzano
###### [ 7.55% ] [ 15107 votos ] Leo Péricles
###### [ 7.54% ] [ 15085 votos ] Simone Tebet
###### [ 7.53% ] [ 15054 votos ] Vera Lúcia
###### [ 7.47% ] [ 14946 votos ] Jair Messias Bolsonaro
###### [ 7.47% ] [ 14934 votos ] Eymael
###### [ 7.46% ] [ 14911 votos ] Soraya Thronicke
###### [ 7.42% ] [ 14834 votos ] Padre Kelmon
###### [ 7.41% ] [ 14828 votos ] Felipe D'Avila
