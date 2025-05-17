import pandas as pd
import csv

def process_sped_file(file):
    headers = {}
    all_lines = []

    try: 
        with open(file, 'r', encoding='latin-1') as f:
            for line in f:
                all_lines.append(line)
                print(line)
    except FileNotFoundError:
        return f"Erro: Arquivo '{file}' não encontrado."
    except Exception as e:
        return f"Error reading file: {e}"