#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class SJF(object):

	def __init__(self, lines):
		# Copia de 'lines' para nao modificar o arquivo original
		inputs = copy.deepcopy(lines)

		# String com os valores de: retorno, resposta e espera
		self.output = ""

		# Converte todos os valores de entrada em inteiros
		for i,line in enumerate(inputs):
			inputs[i] = []
			inputs[i].append(int(line.split()[0]))
			inputs[i].append(int(line.split()[1]))


		# Tempo de retorno medio
		return_time = 0
		# Calcula o tempo de retorno para cada processo
		return_time_to_process = 0

		# Tempo de resposta medio
		response_time = 0
		# Calcula o tempo de respota para cada processo
		response_time_to_process = 0

		# Tempo de espera medio
		wait_time = 0
		# Calcula o tempo de espera para cada processo
		wait_time_to_process = 0

		# Tempo corrente e usado para calcular o tempo atual
		current_time = 0

		# Se a primeira entrada nao chegar no tempo zero, o tempo corrente e atualizado
		if inputs[0][0] > current_time:
			current_time = inputs[0][0]

		# Quantidade de entradas
		size_inputs = len(inputs)

		# Flag que indica o primeiro processo
		flag = True

		# Para quando todas as entradas sao atendidas
		while inputs:

			# Lista com tempos de execucao
			input_exec = []

			for j,inp_aux in enumerate(inputs):
				# Verifica se o tempo de chegada do processo e menor do que o tempo corrente
				if inp_aux[0] <= current_time:
					# Adiciona entrada como uma das possiveis a ser executada
					input_exec.append(inp_aux[1])
				# Nao precisa terminar de percorrer, pois todos os outros tempos de chegada sao maiores
				else:
					break

			# Recebe a posicao da entrada com o menor job
			input_position = input_exec.index(min(input_exec))
			# Menor job com tempo de chegada menor ou igual ao tempo corrente
			inp = inputs[input_position]
			# Retira o job da lista de entradas
			inputs.pop(input_position)


			# Primeira entrada nao espera nenhum outro processo
			if flag:
				# Tempo de retorno do processo e usado para calcular o tempo de retorno de cada processo
				return_time_to_process = inp[1]

				#Primeiro tempo de resposta e zero
				#Primeiro tempo de espera e zero

				# O proximo processo nao e mais o primeiro
				flag = False
			else:
				# Testa se houve tempo ocioso
				if current_time > inp[0]:
					# Tempo esperado ate agora + tempo para execucao
					return_time_to_process = current_time - inp[0] + inp[1]

					# Tempo de respota e o tempo esperado
					response_time_to_process = current_time - inp[0]

					# Tempo esperado para execucao
					wait_time_to_process = current_time - inp[0]
				else:
					# Tempo corrente atualizado para o tempo de todos processos executados + tempo ocioso
					current_time = inp[0]

					# Nao houve espera
					return_time_to_process = inp[1]
					response_time_to_process = 0
					wait_time_to_process = 0

			# Tempo corrente e igual ao somatorio do tempo de execucao de todos os processos ate aqui
			current_time += inp[1]
			# Somatorio com o tempo de retorno de cada entrada
			return_time += return_time_to_process

			# Somatorio com o tempo de resposta de cada entrada
			response_time += response_time_to_process

			# Somatorio com o tempo de resposta de cada entrada
			wait_time += wait_time_to_process


		# Calculado o tempo de retorno medio e convertido para string
		return_time = str(return_time / size_inputs)
		# Calculado o tempo de resposta medio e convertido para string
		response_time = str(response_time / size_inputs)
		# Calculado o tempo de espera medio e convertido para string
		wait_time = str(wait_time / size_inputs)

		# Troca ponto por virgula
		self.output += return_time.replace('.', ',')
		self.output += " " + response_time.replace('.', ',')
		self.output += " " + wait_time.replace('.', ',')
