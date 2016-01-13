#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, copy

class FCFS(object):

	def __init__(self, lines):
		# Copia de 'lines' para nao modificar o arquivo original
		inputs = copy.deepcopy(lines)

		# Lista de 3 posicoes para os valores de retorno, resposta e espera
		self.output = [0,0,0]

		# Converte todos os valores de entrada em inteiros
		for i,line in enumerate(inputs):
			inputs[i] = []
			inputs[i].append(int(line.split()[0]))
			inputs[i].append(int(line.split()[1]))

		# Tempo de retorno medio
		return_time = 0

		# Tempo corrente e usado para calcular o tempo atual
		current_time = 0

		# Tempo de retorno e usado para calcular o tempo de retorno para cada processo
		return_time_to_process = 0

		for i,inp in enumerate(inputs):
			# Primeira entrada nao espera nenhum outro processo
			if i == 0:
				# Tempo de retorno do processo e usado para calcular o tempo de retorno de cada processo
				return_time_to_process = inp[1]
			else:
				# Testa se houve tempo ocioso
				if current_time > inp[0]:
					# Tempo esperado ate agora + tempo para execucao
					return_time_to_process = current_time - inp[0] + inp[1]
				else:
					# Tempo corrente atualizado para o tempo de todos processos executados + tempo ocioso
					current_time = inp[0]
					# Nao houve espera
					return_time_to_process = inp[1]

			# Tempo corrente e igual ao somatorio do tempo de execucao de todos os processos ate aqui
			current_time += inp[1]
			# Somatorio com o tempo de retorno de cada entrada
			return_time += return_time_to_process


		# Calculado o tempo de retorno medio
		self.output[0] = return_time / (i + 1)
