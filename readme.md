## Aprendizagem Supervisionada de Doenças Cardíacas

Utilização do banco de dados Cliveland para executar os seguites experimentos de aprendizagem supervisionada:

1) Carregue e configure o dataset dividindo-o em dataset de treinamento e dataset de testes. Descreva detalhadamente a estratégia utilizada para dividir o dataset.

2) Execute o treinamento utilizando o algoritmo KNN. Explique todas as escolhas de hiperparâmetros utilizados no treinamento.

3) Execute os testes com o modelo treinado e faça medição no mínimo de acurácia e precisão.

4) Implemente uma rede neural supervisionada e treine com o mesmo dataset utilizado para o CNN. Explique todas as escolhas de hiperparâmetros utilizados no treinamento

5) Execute os testes com a rede neural treinada medindo, no mínimo, acurácia e precisão.

## Requisitos
- [sklearn 1.2.2](https://pypi.org/project/sklearn)
- [python 3.8.10](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
- [pandas 0.25.3](https://pandas.pydata.org/docs/getting_started/install.html#installing-from-pypi)
- [matplotlib 3.6.2](https://matplotlib.org/stable/index.html#installation)
- [scikit-learn 1.2.2](https://scikit-learn.org/stable/install.html#installing-scikit-learn)
- [ubuntu 20.04.02](https://ubuntu.com/download/desktop)
- [visual studio code 1.78.2 ](https://code.visualstudio.com/download)
## Descrição do Dataset:

É um dataset rotulado, tendo o atributo target como rótulo. O target tem valor 0 quando não há presença de doença cardíaca e 1 quando há presença de doença cardíaca.  

Os demais atributos estão descritos a seguir:


| Parâmetros  | Valores|
| ------------- | ------------- |
| Idade | Número inteiro |
| Sexo  | 1 - masculino; 0 - feminino |
| Colesterol sérico (chol) | em mg/dl |
| Pressão arterial em repouso (trestbps) | número inteiro em mmHg |
| Frequência cardíaca máxima alcançada (thalach) | número inteiro |
| Talassemia | 1 - normal; 2- defeito corrigido; 3 - defeito reversível |
| Angina (dor no peito) induzida por exercício (exang) | 0 - Sim; 1 - Não |
| Açúcar no sangue em jejum (fbs) | 1 - se > 120 mg/dl; 0 - se <= 120 mg/dl |
| Depressão de ST induzida por exercício em relação ao repouso (oldpeak): | número inteiro |
| Pico do segmento ST durante o exercício (slope): | 0 - ascendente; 1 - plana; 2 - descendente |
| Número de vasos principais (0–3) coloridos por fluoroscopia (ca):  | número inteiro de 0 a 3  |
| ECG em repouso (restecg) |  0 - normal; 1 - anomalia na onda ST-T; 2 - hipertrofia ventricular esquerda |
| Chest-paint type (cp)(tipo da dor no peito) |  0 - típica; 1 - atípica; 2 - não-anginosa; 3- assíntótica |
