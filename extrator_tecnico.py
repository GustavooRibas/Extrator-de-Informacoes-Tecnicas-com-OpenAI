import json
import openai
from openai import OpenAI
import os

# ============================================
# Extrator de Informações Técnicas com OpenAI
# ============================================
# Autor: Gustavo Rodrigues Ribeiro
# Descrição: Esta aplicação utiliza um modelo de linguagem da OpenAI
# para analisar relatórios técnicos de manutenção e extrair informações
# estruturadas em JSON, de forma robusta e interpretável por máquina.
# ============================================

# Configuração da chave de API da OpenAI a partir de variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "SUA_API_KEY_AQUI (Não Recomendado)"))

def construir_prompt(texto):
    """
    Monta o prompt a ser enviado para o modelo da OpenAI com instruções detalhadas
    sobre como extrair os dados do relatório técnico e estruturá-los em JSON.
    """
    return f"""
Você é um assistente técnico especializado. Extraia do relatório a seguir as informações estruturadas no seguinte esquema JSON:

{{
  "equipamento": {{
    "nome": string,
    "modelo": string,
    "fabricante": string
  }},
  "problemas": [string],
  "especificacoes_tecnicas": [string],
  "acoes_realizadas": [string],
  "acoes_recomendadas": [string],
  "componentes_mencionados": [string],
  "informacoes_ambiguas_ou_incompletas": [string]
}}

Instruções:
- Utilize frases completas e linguagem técnica clara.
- Observe que, geralmente, temos o nome do equipamento antes do modelo e fabricante, assim adicione o nome do equipamento.
- Inclua unidades de medida e códigos de peças sempre que disponíveis.
- Cite nomes de componentes, parâmetros técnicos, valores numéricos e substâncias utilizadas (ex: gás, produto químico).
- Considere como especificações técnicas qualquer variação de temperatura, pressão, desempenho, ruído ou eficiência.
- Relacione em "componentes_mencionados" todas as peças ou conjuntos técnicos citados, mesmo que não estejam diretamente ligados aos problemas ou ações.
- Evite repetições entre os campos (ex: problemas ≠ especificações).
- Ações realizadas e recomendadas devem ser claras e distintas.
- Caso haja lacunas, incertezas ou falta de contexto técnico, registre-as em "informacoes_ambiguas_ou_incompletas".
- O JSON gerado deve ser válido, bem indentado e conter apenas os dados solicitados.

Relatório técnico:
{texto}

Retorne exclusivamente o JSON estruturado.
"""

def extrair_informacoes(texto):
    """
    Envia o prompt com o relatório técnico para o modelo da OpenAI (GPT-4 ou GPT-3.5-Turbo)
    e tenta converter a resposta em um dicionário Python (via JSON).
    """
    prompt = construir_prompt(texto)

    try:
        # Chamada à API de chat da OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )

        # Extrai apenas o conteúdo textual da resposta
        conteudo = response.choices[0].message.content

        try:
            # Tenta fazer o parsing do conteúdo como JSON
            return json.loads(conteudo)
        except json.JSONDecodeError as e:
            # Caso o JSON esteja malformado, exibe o conteúdo para depuração
            print("[ERRO] JSON inválido retornado pelo modelo. Veja o conteúdo abaixo:\n")
            print(conteudo)
            return {}

    except Exception as e:
        # Tratamento de erro em caso de falha na chamada da API
        print("[ERRO] Falha ao acessar a API da OpenAI:", e)
        return {}

def salvar_json_em_arquivo(dados, nome_arquivo="saida.json"):
    """
    Salva o conteúdo do dicionário Python no formato JSON formatado
    em um arquivo com codificação UTF-8.
    """
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def ler_documento_tecnico(caminho="documento_tecnico.txt"):
    """
    Lê o conteúdo de um relatório técnico a partir de um arquivo de texto (.txt).
    Caso o arquivo não seja encontrado, retorna string vazia.
    """
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{caminho}' não encontrado.")
        return ""

# Execução principal do script
if __name__ == "__main__":
    print("\n[INFO] Lendo documento técnico...")
    texto = ler_documento_tecnico()

    # Verifica se o arquivo está vazio
    if not texto.strip():
        print("[ABORTADO] Nenhum conteúdo encontrado para processar.")
        exit(1)

    print("[INFO] Extraindo informações com modelo LLM...")
    resultado = extrair_informacoes(texto)

    # Se o JSON foi extraído com sucesso, salva em arquivo
    if resultado:
        print("[INFO] Salvando resultado em 'saida.json'...")
        salvar_json_em_arquivo(resultado)
        print("[SUCESSO] Informações extraídas com sucesso. Veja o arquivo 'saida.json'.")
    else:
        print("[FALHA] Não foi possível gerar um JSON estruturado. Verifique os logs acima.")