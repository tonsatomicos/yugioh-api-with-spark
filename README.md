# <p align="center">Projeto de Processamento Distribuído<br>API Yu-Gi-Oh! TCG</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=...&color=GREEN&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto foi concebido como parte de um desafio durante a disciplina de Processamento Distribuído, no curso de pós-graduação em Engenharia de Dados, na Universidade de Fortaleza (Unifor).

O desafio consistia em desenvolver um projeto utilizando Spark. Optei por consumir e processar os dados obtidos através da API do Yu-Gi-Oh! TCG.

Para realizar o projeto, utilizei Docker para configurar e gerenciar os recursos necessários para o Spark, além de executar o pipeline. Usei <code>Requests</code> para a extração dos dados da API do Yu-Gi-Oh! TCG e <code>PySpark</code> para o processamento dos dados, que foram salvos em arquivos parquet particionados.

## Etapas

## Estrutura

 Utilizando Docker para criar os containers necessários e configurar o ambiente de execução. Utilizei o arquivo <code>pyproject.toml</code> como fonte das dependências para instalação na imagem Docker. 

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

Como mencionado anteriormente, optei por desenvolver o projeto utilizando a infraestrutura fornecida pelos containers Docker. Todo o ambiente está configurado para fácil replicação. Não abordarei os detalhes técnicos aqui, mas sinta-se à vontade para adaptar o projeto conforme necessário, com ou sem Docker.

No entanto, faz sentido que, ao tentar replicar este projeto, você siga a mesma abordagem que eu e utilize Docker. Isso garantirá que o ambiente e as dependências estejam configurados corretamente, proporcionando uma experiência mais consistente e eficiente.

### Como usar?

Acesse a pasta raiz do projeto e execute o seguinte comando para subir a imagem e os containers: 

```bash
docker compose -f docker-compose.yml up -d --scale spark-worker=2
```

Este comando iniciará os containers e escalará o número de workers do Spark conforme definido no arquivo <code>docker-compose.yml</code>.

## Configurações do Projeto - Parte 2

O <code>docker-compose.yml</code> está configurado para mapear as principais pastas do projeto.

Acesse o container master usando o VSCode, o terminal do Windows/Linux com Docker Engine ou o Docker Desktop. Navegue até a pasta /opt/spark/yugioh-with-spark e execute:

```bash
python yugioh-with-spark/pipeline/pipeline_main.py
```

Isso irá executar o pipeline principal do projeto.

## Conclusão

Após executar o comando, observe os <code>logs</code> para acompanhar o andamento do processamento e verifique a pasta <code>data/output</code> para conferir os resultados gerados.

## Considerações Finais

- A documentação pode não estar totalmente detalhada, e um certo nível de conhecimento pode ser necessário para entender o projeto.
- Tentei aplicar os conceitos de SOLID neste projeto, o que pode fazer com que a estrutura pareça um pouco confusa.
<hr>

![Image](https://i.imgur.com/p4vnGAN.gif)
