# Extrator de Informações Técnicas com LLM (OpenAI API)

## Autor: Gustavo Rodrigues Ribeiro

## 📄 Descrição Geral

Este projeto tem como objetivo a criação de uma aplicação baseada em modelos de linguagem (LLMs), especificamente a API da OpenAI, para realizar **análise automatizada de relatórios técnicos**. O foco está na extração precisa e estruturada de dados críticos a partir de arquivos de texto contendo informações técnicas sobre manutenção de equipamentos industriais.

A saída do processo é um arquivo JSON interpretável por máquina, ideal para integração com bancos de dados, dashboards ou sistemas de manutenção assistida por IA.

---

## Funcionalidades

- Leitura de relatórios técnicos em `.txt`
- Extração automática de:
  - Nome, modelo e fabricante do equipamento
  - Problemas operacionais relatados
  - Especificações técnicas como temperatura, pressão, eficiência, códigos de peças
  - Ações de manutenção já realizadas
  - Recomendações futuras para manutenção preventiva ou corretiva
  - Componentes mencionados
  - Informações ambíguas, vagas ou incompletas
- Saída JSON clara, indentada e padronizada
- Robustez contra falhas de interpretação e JSONs malformados

---

## Tecnologias Utilizadas

- **Python 3.8+**
- **OpenAI GPT-4/GPT-3.5-Turbo API** (`openai` library)
- Estrutura modular de funções e boas práticas de engenharia de software

---

## Estrutura do Projeto

```
├── extrator_tecnico.py         # Script principal da aplicação
├── documento_tecnico.txt       # Relatório técnico de entrada
├── saida.json                  # Saída gerada com os dados estruturados
├── README.md                   # Instruções e documentação detalhada
```

---

## Como Executar o Projeto

Certifique-se de que você possui o Python instalado (recomendado Python 3.10+).

No repositório do projeto:

### 1. Crie um ambiente virtual (opcional, mas recomendado)

Criando ambiente virtual:

```bash
python -m venv venv
```

Acessando ambiente virtual:

Em Sistemas Unix:

```bash
source venv/bin/activate
```

Em Sistemas Windows (CMD):

```bash
venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install openai
```

### 3. Configurar a chave de API da OpenAI

Você pode definir a chave diretamente no script ou via variável de ambiente:

Em Sistemas UNIX:

```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

Em Sistemas Windows (CMD):

```bash
set OPENAI_API_KEY=sua_chave_aqui
```

### 4. Executar o script

```bash
python extrator_tecnico.py
```

A saída será salva no arquivo `saida.json` na raiz do projeto.

---

## Exemplo de Saída JSON (simulada)

```json
{
    "equipamento": {
        "nome": "Chiller",
        "modelo": "CR-420",
        "fabricante": "CoolTech"
    },
    "problemas": [
        "Queda de eficiência de aproximadamente 30% nos últimos 15 dias",
        "Aumento no ruído de funcionamento",
        "Temperatura de saída 5°C acima do parâmetro normal",
        "Compressor secundário com desgaste excessivo nas válvulas de sucção",
        "Vazamento de gás refrigerante R-410A no circuito principal (pressão 15% abaixo do nominal)",
        "Condensador com acúmulo de sujeira reduzindo capacidade de troca térmica"
    ],
    "especificacoes_tecnicas": [
        "Eficiência reduzida em 30%",
        "Temperatura de saída 5°C acima do normal",
        "Ruído de funcionamento aumentado",
        "Pressão do gás refrigerante R-410A 15% abaixo do nominal"
    ],
    "acoes_realizadas": [
        "Substituição das válvulas de sucção do compressor (peças: VS-42B e VS-42C)",
        "Reparo no ponto de vazamento localizado na conexão CC-12",
        "Recarga de 2,4kg de gás R-410A",
        "Limpeza do condensador com produto químico CR-Clean"
    ],
    "acoes_recomendadas": [
        "Programar substituição completa do compressor secundário em até 60 dias",
        "Aumentar frequência de limpeza do condensador para ciclos mensais",
        "Instalar sensor de pressão adicional no ponto CC-12 para monitoramento contínuo"
    ],
    "componentes_mencionados": [
        "Compressor secundário",
        "Válvulas de sucção",
        "Circuito principal",
        "Gás refrigerante R-410A",
        "Condensador",
        "Conexão CC-12",
        "Produto químico CR-Clean"
    ],
    "informacoes_ambiguas_ou_incompletas": []
}
```

---

## Considerações Técnicas e Sugestões de Expansão

- O prompt é cuidadosamente construído para garantir estrutura, contexto técnico e extração fiel de dados.
- É possível estender este projeto para ler arquivos PDF, DOCX ou usar OCR para documentos digitalizados.
- A integração com um banco de dados ou dashboard web pode viabilizar análise em escala de relatórios industriais.
- Uma camada de pós-processamento com validações semânticas pode ser integrada para aumento de confiabilidade.