import subprocess
import sys
import os

comando = ["java",
       "-cp",
       "./libs/xercesImpl-2.12.2.jar:./libs/jflaplib-cli-1.3-bundle.jar",
       "es.usc.citius.jflap.cli.CommandLine",
       "run"]

pasta_atual = sys.argv[1]

pasta_automatos = "/automatos/"
pasta_entradas = "/entradas/"
pasta_saidas = "/saidas/"

n_atutomatos = len(os.listdir(pasta_atual+pasta_automatos))

for i in range(n_atutomatos):
    n = str(i+1)
    n_atutomato = pasta_atual+pasta_automatos+n+".jff"
    n_entrada = pasta_atual+pasta_entradas+n+".txt"
    n_saida = pasta_atual+pasta_saidas+n+".txt"

    with open(n_entrada, "r", encoding="utf-8") as f1, \
        open(n_saida, "r", encoding="utf-8") as f2:
    
        entradas = [linha.strip() for linha in f1]
        saidas = [linha.strip() for linha in f2]
    
    tamanho = len(entradas)
    
    if(tamanho == len(saidas)):
        corretos = 0
        
        print("Teste do automato: " + n + ".jff")
        
        for j in range(tamanho):
            if (entradas[j] == ""):
                entradas[j] = " "
            cmd = comando + [n_atutomato, entradas[j]]
            # print(cmd)
            resultado = subprocess.run(cmd, capture_output=True, text=True)
            resultado = resultado.stdout
            if resultado.strip() == saidas[j].strip():
                corretos += 1
            else:
                print(resultado)
                print(saidas[j])
                break
        if (corretos == tamanho):
            print("OK")
        else:
            print("ERRO: " + str(corretos) + " corretos de: " + str(tamanho))
