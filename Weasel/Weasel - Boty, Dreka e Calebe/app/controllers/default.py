from flask import render_template, flash, url_for, redirect, Flask, send_file, request, send_from_directory
from datetime import datetime
from app import app
import config as cfg
import sys, random

from app.models.forms import Form

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = Form()
    if form.target.data == None and form.mutation.data == None and form.gen_size.data == None:
        return render_template("index.html", form = form)
    else:
        result = []
        #target = list("METHINKS IT IS LIKE A WEASEL")   # Frase alvo
        target = list(str(form.target.data))
        print(form.target.data)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "        # Todas as mutações possíveis, incluindo espaço
        #n_offspring = 50                                # Descendentes por geração
        n_offspring = form.gen_size.data
        print(form.gen_size.data)
        #mut_rate = 0.08
        mut_rate = form.mutation.data
        print(form.mutation.data)                        # Taxa de mutação
        best_offspring = []                             # Armazena o descendente mais próximo, por geração
                                                        # Lista vazia, pra comparar a melhor geração ao alvo
        # Constroi aleatoriamente a entrada
        parent = []
        for i in range(len(target)):
            parent.append(random.choice(alphabet))
            # Loop principal. Constrói as gerações e seleciona o melhor p proxima geração, para quando a geração iguala ao alvo
        gen = 0
        while best_offspring != target:
            gen = gen + 1
                # Números de mutações boas, más e neutras dessa geração
            n_beneficial = n_detrimental = n_neutral = num_mut = 0.0
                # Conta quantos "filhos" na geração atual são exatamente iguais aos "pais"
            num_unchanged = n_offspring
                #Constroi a lista de gerações que podem conter mutações
            kid_list = []
            for i in range(n_offspring):
                    # Copia o valor do filho
                kid = parent[:]
                # Itera as posições do filho, para cada posição que possa ser mutada
                kid_changed = False
                for pos in range(len(kid)):
                        # Muta de acordo com a % de mutação
                    if random.random() < mut_rate:
                        kid_changed = True
                        num_mut += 1
                            # Seleciona um novo caracter aleatório, que é diferente do atual.
                        old_symbol = parent[pos]
                        possible_new_symbols = set(alphabet) - set(old_symbol)
                        new_symbol = random.choice(list(possible_new_symbols))
                            # Muta o filho
                        kid[pos] = new_symbol
                            # Checa se foi benéfico, maléfico ou neutra a mudança, e atualiza a geração
                        if old_symbol == target[pos]:           # Se uma letra que já estava certa foi mutada, maléfica
                            n_detrimental += 1
                        elif new_symbol == target[pos]:         # Se uma letra errada foi mutada para uma correta, benéfica
                            n_beneficial += 1
                        else:                                   # Se uma letra errada foi mutada para outra letra errada, neutra.
                            n_neutral += 1
                # Se foi mutada, então não parece como o antecessor
                if kid_changed:
                    num_unchanged -= 1
                # Adiciona (possívelmente) um filho mutado para lista de filhos atuais
                kid_list.append(kid)

            # Procura o mais similar ao alvo
            smallest_dif = len(target) + 1
            for kid in kid_list:
                    # Procura o número de posições que são diferentes entre o filho e o alvo.
                dif = 0.0
                for pos in range(len(target)):
                    if kid[pos] != target[pos]:
                        dif = dif + 1
                    # Mantém o melhor filho encontrado
                if dif < smallest_dif:
                    smallest_dif = dif
                    best_offspring = kid
                # Usa o melhor caso como próximo pai da próxima geração
            parent = best_offspring
                # Imprime la puera toda
            fitness = (len(target)-smallest_dif)/len(target)            # % de similaridade entre filho e alvo
            ben_frac = n_beneficial/num_mut
            detr_frac = n_detrimental/num_mut
            neu_frac = n_neutral/num_mut
            result_string = ""
            for pos in range(len(target)):
                if best_offspring[pos] == target[pos]:
                    result_string += best_offspring[pos]
                else:
                    result_string += best_offspring[pos].lower()
            flash("Gen: %4d   **   %s      **     Dif: %3d - Fit: %.4f - Bene: %.4f - Mal: %.4f - Neu: %.4f  - NãoMutadas: %3d" % (gen, result_string, smallest_dif, fitness, ben_frac, detr_frac, neu_frac, num_unchanged))
            #result.append(x)
    return render_template("result.html", form = form)