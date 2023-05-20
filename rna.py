# Aluno: Iago Manoel Brito de Sá Vaz da Silva
# Matrícula: 202010135
#
# 1. a rede neural é executada com a1(x, w), sendo x o valor de entrada e w a matriz de pesos
# 2. as funções delta_i calculam o delta_i para o a_i
# 3. saídas e deltas são as seguintes
#    x = 0.00
#    y = 0.50
#    z_1 = 0.0759
#    z_2 = 0.0000
#    z_3 = 0.5000
#    z_4 = 0.5000
#    z_5 = 0.0000
#
#    delta_1 = 0.0297
#    delta_2 = 0.0000
#    delta_3 = -0.0297
#    delta_4 = -0.0074
#
#    x = 1.00
#    y = 0.10
#    z_1 = 0.2929
#    z_2 = 0.8807
#    z_3 = 0.8808
#    z_4 = 0.0000
#    z_5 = 1.0000
#
#    delta_1 = -0.0400
#    delta_2 = -0.1199
#    delta_3 = 0.0042
#    delta_4 = 0.0000
#
# 4. a função train executa o algoritmo gradient descent utilizando os delta_i anteriormente criados
# 5. a função train_all_samples treina a rede por n épocas
#    os novos pesos após 200 épocas são os seguintes, sendo linhas e colunas indexadas a base 1:
#
#    w = [
#         [0, 0, 0, 0, 0],
#         [2.136086526013715, 0, 0, 0, 0],
#         [0.38303240382459347, -0.01176722774891218, 0, 0, 0],
#         [1.5813802768661815, -2.8772220950562635, 0, 0, 0],
#         [0, 0, 2.6134529089241734, -10.106010914813892, 0],
#        ]
#
#    os plots de erro estão disponíveis ao executar este arquivo
#    tenha matplotlib instalado
#
#    em anexo está o gráfico de erro e a animação da evolução da saída da rede
#    erro-e-previsao.mp4

import math
import copy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

w = [#   1   2  3   4   5
    [0,  0,  0, 0,  0,  0], # 0
    [0,  0,  0, 0,  0,  0], # 1
    [0,  3,  0, 0,  0,  0], # 2
    [0, -4,  1, 0,  0,  0], # 3
    [0, -1, -3, 0,  0,  0], # 4
    [0,  0,  0, 2, -10, 0]  # 5
]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return 0 if x < 0 else x

def deriv_sigmoid(x):
    return x * (1 - x)

def deriv_relu(x):
    return 0 if x <= 0 else 1

def a5(x, w):
    return x

def a4(x, w):
    return sigmoid(w[5][4] * a5(x, w))

def a3(x, w):
    return sigmoid(w[5][3] * a5(x, w))

def a2(x, w):
    return relu(w[3][2] * a3(x, w) + w[4][2] * a4(x, w))

def a1(x, w):
    return sigmoid(w[3][1] * a3(x, w) + w[2][1] * a2(x, w) + w[4][1] * a4(x, w))

def delta1(x, w, yt):
    y1 = a1(x, w)
    return deriv_sigmoid(y1) * (yt - y1)

def delta2(x, w, yt):
    y2 = a2(x, w)
    return deriv_relu(y2) * w[2][1] * delta1(x, w, yt)

def delta3(x, w, yt):
    y3 = a3(x, w)
    s = w[3][2] * delta2(x, w, yt) + w[3][1] * delta1(x, w, yt)
    return deriv_sigmoid(y3) * s

def delta4(x, w, yt):
    y4 = a4(x, w)
    s = w[4][2] * delta2(x, w, yt) + w[4][1] * delta1(x, w, yt)
    return deriv_sigmoid(y4) * s

y = [a1, a2, a3, a4, a5]
delta = [delta1, delta2, delta3, delta4]

def test(x, w, yt):
    print(f'{x = :.2f}')
    print(f'y = {yt:.2f}')
    for i, o in enumerate(y):
        print(f'z_{i+1} = {o(x, w):.4f}')
    print()
    for i, d in enumerate(delta):
        print(f'delta_{i+1} = {d(x, w, yt):.4f}')
    print()

test(0, w, 0.5)
test(1, w, 0.1)

def err(x, w, yt):
    return (a1(x, w) - yt) ** 2 / 2

train_data = [
    (-3,   0.73212),
    (-2,   0.7339),
    (-1,   0.7838),
    (-0.5, 0.8903),
    (0,    0.982),
    (0.5,  0.8114),
    (1.0,  0.5937),
    (1.5,  0.5219),
    (2.0,  0.5049),
    (3.0,  0.5002)
]

# treinamento usando gradient descent
def train(x, w, yt, rate=1):
    nw = copy.deepcopy(w)
    for i in range(len(w)):
        for j in range(len(w[i])):
            if nw[j][i] == 0: continue
            nw[j][i] = w[j][i] + rate * delta[i-1](x, w, yt) * y[j-1](x, w)
    return nw

# realiza n rodadas de treino contra um conjunto de dados
def train_all_samples(n=10, nw=w):
    preds = []
    all_errs = []

    for _ in range(n):
        pred = []
        errs = []

        for x, yt in train_data:
            nw = train(x, nw, yt)
            pred.append((x, a1(x, nw)))
            errs.append(err(x, nw, yt))

        preds.append(pred)
        all_errs.append(errs)

    return nw, preds, all_errs

def printw(w):
    print('w = [')
    for i in range(1, len(w)):
        print(f'  {w[i][1:]},')
    print(']')

def plot():
    nw, preds, all_errs = train_all_samples(200)

    errs = []
    for err in all_errs:
        errs.extend(err)
    printw(nw)

    fig, ax = plt.subplots(nrows=2)
    ln, = ax[1].plot([], [])
    ax[1].set_xlim(-3, 3)
    ax[1].set_ylim(0, 1)

    def update(frame):
        xdata = []
        ydata = []
        for x, y in preds[frame]:
            xdata.append(x)
            ydata.append(y)
        ln.set_data(xdata, ydata)
        return ln,

    ax[0].plot(errs)

    ani = FuncAnimation(fig, update, frames=len(preds), interval=20, blit=True)
    # ani.save('erro-e-previsao.mp4')

    plt.show()

plot()
