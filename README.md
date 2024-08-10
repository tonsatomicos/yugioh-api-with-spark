# <p align="center">Projeto de Processamento Distribuído<br>API Yu-Gi-Oh! TCG</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=N/A&color=GREEN&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto foi desenvolvido como parte de um desafio na disciplina de Processamento Distribuído do curso de pós-graduação em Engenharia de Dados na Universidade de Fortaleza (Unifor). 

O objetivo principal do desafio era explorar e aplicar o Apache Spark para processamento de dados distribuído.

Como caso de uso, escolhi trabalhar com dados da API do Yu-Gi-Oh! TCG. Utilizei a biblioteca <code>requests</code> para a extração dos dados e o <code>pyspark</code> para a transformação e carregamento, todos executados em um ambiente Docker configurado com o Spark.

## Etapas

## Estrutura

A estrutura do projeto foi organizada para ser replicável e de fácil manutenção. Utilizei Docker para criar os containers necessários e configurar o ambiente de execução. O arquivo <code>pyproject.toml</code> foi utilizado para gerenciar as dependências.

### Versão do Python
```bash
3.11.9-bullseye
```

### Dependências | Produção

- pyspark
- requests
- loguru

### Dependências | Desenvolvimento

- ipykernel
- flake8
- black
- isort
- sparksql_magic
- pre-commit

## Configuração e Execução

Como mencionado anteriormente, optei por desenvolver o projeto utilizando a infraestrutura fornecida pelos containers Docker. Todo o ambiente está configurado para fácil replicação. Não abordarei os detalhes técnicos aqui, mas sinta-se à vontade para adaptar o projeto, com ou sem Docker.

No entanto, faz sentido que, ao tentar replicar este projeto, você siga a mesma abordagem que eu e utilize Docker. Isso garantirá que o ambiente e as dependências estejam configuradas corretamente, proporcionando uma experiência mais consistente e eficiente.

### Como usar?

#### Clone o Repositório

Execute o seguinte comando:

```bash
git clone https://github.com/tonsatomicos/yugioh-api-with-spark.git
```

#### Inicie os Containers

Navegue até a pasta raiz do projeto e execute o seguinte comando para iniciar os containers Docker: 

```bash
docker compose -f docker-compose.yml up -d --scale spark-worker=2
```

> Nota: Se estiver no Windows, certifique-se de que os arquivos <code>Dockerfile</code>, <code>docker-compose.yml</code> e <code>entrypoint.sh</code> estejam com a formatação LF, e não CRLF.

Este comando iniciará os containers e escalará o número de workers do Spark conforme definido no arquivo <code>docker-compose.yml</code>.

#### Execute o Pipeline Principal

Acesse o container master utilizando o terminal ou VSCode. Navegue até a pasta <code>/opt/spark/yugioh-with-spark</code> e execute:

```bash
python yugioh-with-spark/pipeline/pipeline_main.py
```

## Conclusão

Monitore o andamento do pipeline acompanhando os logs gerados durante a execução. Eles serão armazenados na pasta <code>/logs</code>, e os resultados do processamento estarão disponíveis na pasta <code>/data/output</code>.

Você também pode monitorar o status dos workers e das aplicações no Spark Master através do link http://localhost:9091/ e visualizar os logs das aplicações completadas no History Server em http://localhost:18081/.

## Considerações Finais

- A documentação pode não estar totalmente detalhada, e um certo nível de conhecimento pode ser necessário para entender o projeto.
- Um Jupyter Notebook está disponível na pasta <code>/notebook</code>, oferecendo uma visão simplificada e mais direta do projeto.
- O projeto foi estruturado utilizando os princípios SOLID, visando manter uma arquitetura limpa e extensível.
<hr>

![Image](https://i.imgur.com/p4vnGAN.gif)
