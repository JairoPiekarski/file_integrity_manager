# Python File Integrity Monitor (FIM) 🛡️

Este projeto é uma ferramenta de monitoramento de integridade de arquivos em tempo real. Ele utiliza criptografia para garantir que qualquer modificação, criação ou exclusão de arquivos em um diretório crítico seja detectada e reportada instantaneamente.

## 🚀 Funcionalidades

- **Criptografia SHA-256:** Gera uma "impressão digital" única para cada arquivo, tornando impossível alterar o conteúdo sem ser detectado.
- **Monitoramento em Tempo Real:** Varredura cíclica para detectar mudanças no sistema de arquivos.
- **Detecção de Três Estados:**
    - **Novos Arquivos:** Identifica quando arquivos não autorizados são inseridos.
    - **Modificações:** Detecta alterações bit-a-bit em arquivos existentes (útil contra Ransomware).
    - **Remoções:** Alerta se arquivos críticos forem deletados.
- **Otimização de Memória:** Leitura de arquivos em blocos (4096 bytes) para suportar arquivos grandes sem travar o sistema.

## 🛠️ Por que isso é importante?

Em um cenário de cibersegurança, o FIM é essencial para:
1. **Detectar Intrusões:** Invasores costumam modificar arquivos de configuração ou instalar backdoors.
2. **Conformidade (Compliance):** Atende requisitos de normas como PCI-DSS e ISO 27001.
3. **Prevenção de Ransomware:** Identifica a criptografia em massa de arquivos assim que o processo começa.

## 📋 Como usar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/file-integrity-monitor.git](https://github.com/SEU_USUARIO/file-integrity-monitor.git)

2. Execute o script:
   ```
   python fim.py

3. Informe o caminho da pasta que deseja monitorar (Ex: ./config_files ou C:\PastaCritica).

## 🖥️ Exemplo de Logs no Terminal

```
Digite o caminho do diretório a ser monitorado: D:\dev\teste
DEBUG: Tentando acessar: D:\dev\teste
Baseline criada com 1 arquivos.

[+] Iniciando monitoramento em tempo real do diretório: D:\dev\teste
[!] Pressione Ctrl+C para parar o monitoramento.

[NOVO ARQUIVO] D:\dev\teste\Novo(a) Documento de Texto (2).txt foi adicionado.
[NOVO ARQUIVO] D:\dev\teste\teste.txt foi adicionado.
[ARQUIVO DELETADO] D:\dev\teste\Novo(a) Documento de Texto (2).txt foi removido.
[ALTERAÇÃO DETECTADA] D:\dev\teste\teste.txt foi modificado.
[ARQUIVO DELETADO] D:\dev\teste\teste.txt foi removido.

[+] Monitoramento interrompido pelo usuário.

Pressione ENTER para sair...
```

## ⚠️ Aviso Legal

Esta ferramenta deve ser utilizada para monitoramento legítimo e administrativo. Certifique-se de ter as permissões adequadas para monitorar os diretórios escolhidos.
