# <p align="center">Projeto de Processamento Distribuído<br>API Yu-Gi-Oh! TCG</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=...&color=GREEN&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto foi concebido como parte de um desafio durante a disciplina de Processamento Distribuído, no curso de pós-graduação em Engenharia de Dados, na Universidade de Fortaleza (Unifor).

O desafio consistia em desenvolver um projeto utilizando Spark. Optei por consumir e processar os dados obtidos através da API do Yu-Gi-Oh! TCG.

Para realizar o projeto, utilizei <code>Docker</code> para criar e configurar os recursos necessários para o <code>Spark</code>, e para desenvolver e rodar os scripts. Usei <code>Requests</code> para a extração dos dados da <code>API</code> do <code>Yu-Gi-Oh! TCG</code> e <code>PySpark</code> para o processamento dos dados, que foram salvos em arquivos<code>Parquet</code> particionados.

## Etapas

## Estrutura

 Utilizando <code>Docker</code> para criar os containers necessários e configurar o ambiente de execução. Utilizei o arquivo <code>pyproject.toml</code> como fonte das dependências para instalação na imagem <code>Docker</code>. 

### Versão do Python
```bash
3.11.9-bullseye
```

### Dependências | Produção

- pyspark
- requests
- loguru
- pre-commit

### Dependências | Desenvolvimento

- ipykernel
- flake8
- black
- isort

## Configurações do Projeto - Parte 1

Como mencionado anteriormente, optei por desenvolver o projeto utilizando a infraestrutura gerada pelos containers Docker. Todo o ambiente já está pronto para replicação. Não entrarei nos detalhes técnicos, mas sinta-se à vontade para adaptar o projeto sem a necessidade de usar Docker.

### Como usar?

Suba a imagem e os containers. Acesse a pasta do projeto e execute o seguinte comando:

```bash
docker compose -f docker-compose.yml up -d --scale spark-worker=2
```

Este comando iniciará os containers e escalará o número de workers do Spark conforme definido no arquivo <code>docker-compose.yml</code>.


## Configurações do Projeto - Parte 2

O <code>docker-compose.yml</code> está configurado para mapear as pastas de <code>dados(input e output)</code>, <code>logs</code>, <code>notebooks</code>, e <code>yugioh-api-with-spark</code>, que é a pasta dos <code>scripts</code> e o nosso <code>core</code>.

Acesse o container master. Você pode se conectar ao container master usando o VSCode, o terminal do Windows/Linux com Docker Engine ou através do Docker Desktop. Navegue até a pasta <code>/opt/spark/yugioh-with-spark</code> e execute o seguinte comando:

```bash
python yugioh-with-spark/pipeline/pipeline_main.py
```

Isso irá executar o pipeline principal do projeto.

## Conclusão

Após executar o comando, basta observar os <code>logs</code> para verificar o andamento do processamento e checar a pasta <code>data/output</code> para os resultados gerados.

## Considerações Finais

- A documentação pode não estar totalmente detalhada, e um certo nível de conhecimento pode ser necessário para entender o projeto.
- Tentei aplicar os conceitos de SOLID neste projeto, o que pode fazer com que a estrutura pareça um pouco confusa.
<hr>

![Image](https://i.imgur.com/p4vnGAN.gif)
