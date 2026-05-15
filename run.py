# from sikulix import *

# popup("Hello, SikuliX!")

# java -jar sikulixide-2.0.5.jar -r run.py


import subprocess
import os

# CAMINHOS IMPORTANTES
caminho_jar = r"sikulixide-2.0.5.jar"
caminho_script_sikuli = r"C:\caminho\para\meu_script.sikuli"

# Comando para executar o script
comando = ["java", "-jar", caminho_jar, "-r", caminho_script_sikuli]

try:
    # Executa e aguarda a conclusão
    resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
    print("Script executado com sucesso!")
    print("Saída:", resultado.stdout)
except subprocess.CalledProcessError as e:
    print("Erro ao executar o script SikuliX:", e)
    print("Stderr:", e.stderr)