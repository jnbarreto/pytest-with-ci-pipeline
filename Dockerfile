# Use a imagem base oficial do Python
FROM python:3.11-slim

# Atualiza e instala dependências necessárias
RUN apt-get update && apt-get install -y \
    pipx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Adiciona pipx ao PATH
ENV PATH=/root/.local/bin:$PATH

# Instala o Poetry via pipx
RUN pipx install poetry

# Cria e define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de configuração do Poetry
COPY pyproject.toml poetry.lock* /app/

# Instala as dependências do Poetry
RUN poetry install

# Copia todo o conteúdo do repositório para o diretório de trabalho
COPY . /app

# Define o comando para rodar os testes
CMD ["poetry", "run", "pytest"]
