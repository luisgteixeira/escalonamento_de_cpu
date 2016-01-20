#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class RR(object):

    def __init__(self, lines):
        # Copia de 'lines' para nao modificar o arquivo original
        inputs = copy.deepcopy(lines)

        # String com os valores de: retorno, resposta e espera
        self.output = ""

        quantum = 2

        # Converte todos os valores de entrada em inteiros
        for i,line in enumerate(inputs):
        	inputs[i] = []
        	inputs[i].append(int(line.split()[0]))
        	inputs[i].append(int(line.split()[1]))


        # Tempo de retorno medio
        return_time = 0
        # Tempo de resposta medio
        response_time = 0
        # Tempo de espera medio
        wait_time = 0

        # Tempo corrente e usado para calcular o tempo atual
        current_time = 0

        # Se a primeira entrada nao chegar no tempo zero, o tempo corrente e atualizado
        if inputs[0][0] > current_time:
        	current_time = inputs[0][0]

        # Quantidade de entradas
        size_inputs = len(inputs)

        # Flag que indica o primeiro processo
        flag_first = True

        # Lista com os processos em execucao
        input_exec = []

        # Condicao de parada esta no fim
        while True:
            # Copia de 'inputs' para auxiliar a remocao do processos a serem executados
            inputs_aux = copy.deepcopy(inputs)

            for j,inp_aux in enumerate(inputs_aux):
                # Verifica se o tempo de chegada do processo e menor do que o tempo corrente
                if inp_aux[0] <= current_time:
                    # Adiciona entrada na lista das que serao executadas
                    # Os 3 campos a mais sao para calculo do retorno, resposta e espera de cada processo
                    input_exec.append(inp_aux + [0])
                    # Remove o processo que entrou na lista dos que serao executados
                    inputs.remove(inp_aux)
                # Nao precisa terminar de percorrer, pois todos os outros tempos de chegada sao maiores
                else:
                    break

            for i,inp in enumerate(input_exec):
                # Tempo restante de execucao do processo e maior ou igual a 1 quantum
                if inp[1] >= quantum:
                    # Tempo de execucao para o processo
                    execution_time = quantum
                # Tempo restante de execucao do processo e menor que 1 quantum
                else:
                    execution_time = inp[1]

                # Tempo de execucao restante decrementada
                inp[1] -= execution_time

                # Tempo corrente incrementado com o tempo de execucao desse processo
                current_time += execution_time

                for j in range(len(input_exec)):
                    # Tempo de retorno de todos os processos
                    return_time += execution_time
                    if not j == i:
                        # Tempo de espera dos processos que nao estao em execucao
                        wait_time += execution_time

                    # Processo ainda não foi executado
                    if input_exec[j][2] == 0 and j > i:
                        # Tempo de resposta e somado
                        response_time += execution_time
                    # Processo esta sendo executado
                    elif input_exec[j][2] == 0 and j == i:
                        # Processo muda status para executado
                        input_exec[j][2] = 1

                # Exclui os processos que terminaram a execucao
                if inp[1] == 0:
                    input_exec.pop(i)


            # Nao tem mais processos a serem executados
            if not input_exec:
                break

            # DEBUG - DEBUG - DEBUG - DEBUG - DEBUG - DEBUG
            # print("input_exec =", input_exec)
        return_time = str(return_time / size_inputs)
        wait_time = str(wait_time / size_inputs)
        response_time = str(response_time / size_inputs)

        # Troca ponto por virgula
        self.output += return_time.replace('.', ',')
        self.output += " " + response_time.replace('.', ',')
        self.output += " " + wait_time.replace('.', ',')
