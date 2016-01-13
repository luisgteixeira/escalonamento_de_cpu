#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt
from fcfs import *
# from sjf import *
# from rr import *

def main(argv):
    # Recebe o nome do arquivo de entrada
    inputfile = sys.argv[-1]

    if(inputfile == sys.argv[0]): # Verifica se algum arquivo foi recebido
        print('Arquivo nao pode ser lido!!')
    else:
        # Abre o arquivo
        arq = open(inputfile, 'r')
        # Carrega o arquivo em uma lista
        lines = arq.readlines()

        fcfs = FCFS(lines)
        # sjf = SJF(lines)
        # rr = RR(lines)

        print('FCFS', fcfs.output)
        # print('SJF', sjf.output)
        # print('RR', rr.output)

        # Fecha o arquivo
        arq.close()

if __name__ == "__main__":
    main(sys.argv[1:])
