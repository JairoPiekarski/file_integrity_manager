import hashlib
import os
import time

def calculate_sha256(file_path):
    """Calcula o hash SHA-256 de um arquivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Lê o arquivo em blocos para evitar uso excessivo de memória
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    
def create_baseline(directory):
    """Cria uma linha de base de hashes SHA-256 para todos os arquivos em um diretório."""
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_sha256(file_path)
            if file_hash:
                baseline[file_path] = file_hash
    return baseline

def monitor_directory(directory, baseline):
    print(f"\n[+] Iniciando monitoramento em tempo real do diretório: {directory}")
    print("[!] Pressione Ctrl+C para parar o monitoramento.\n")

    try:
        while True:
            time.sleep(5)  # Intervalo de verificação

            current_state = create_baseline(directory)

            for file_path, file_hash in current_state.items():
                if file_path not in baseline:
                    print(f"\033[92m[NOVO ARQUIVO]\033[0m {file_path} foi adicionado.")
                    baseline[file_path] = file_hash
                elif baseline[file_path] != file_hash:
                    print(f"\033[93m[ALTERAÇÃO DETECTADA]\033[0m {file_path} foi modificado.")
                    baseline[file_path] = file_hash
            
            deleted_files = []
            for file_path in baseline:
                if file_path not in current_state:
                    print(f"\033[91m[ARQUIVO DELETADO]\033[0m {file_path} foi removido.")
                    deleted_files.append(file_path)
            
            for f in deleted_files:
                del baseline[f]

    except KeyboardInterrupt:
        print("\n[+] Monitoramento interrompido pelo usuário.")

if __name__ == "__main__":
    target_dir = input("Digite o caminho do diretório a ser monitorado: ")
    
    # Debug: Mostrar o que o Python está tentando ler
    print(f"DEBUG: Tentando acessar: {os.path.abspath(target_dir)}")

    if os.path.exists(target_dir):
        if os.path.isdir(target_dir):
            baseline_hashes = create_baseline(target_dir)
            print(f"Baseline criada com {len(baseline_hashes)} arquivos.")
            monitor_directory(target_dir, baseline_hashes)
        else:
            print("ERRO: O caminho existe, mas não é uma pasta (é um arquivo).")
    else:
        print("ERRO: O diretório especificado não foi encontrado.")
    
    input("\nPressione ENTER para sair...") # Mantém a janela aberta