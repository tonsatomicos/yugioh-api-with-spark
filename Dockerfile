# Base image with Spark and Python
FROM python:3.11.9-bullseye AS spark-base

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      vim \
      nano \
      unzip \
      rsync \
      openjdk-17-jdk \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Spark and Hadoop
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}

# Create directories for Spark and Hadoop
RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

# Download and install Spark
RUN curl https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz -o spark-3.5.1-bin-hadoop3.tgz \
 && tar xvzf spark-3.5.1-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-3.5.1-bin-hadoop3.tgz

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set environment variables for Poetry
ENV PATH="/root/.local/bin:${PATH}"

# Install PySpark and setup environment
FROM spark-base AS pyspark

ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/spark"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

COPY conf/spark-defaults.conf "$SPARK_HOME/conf"

RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH

# Copy entrypoint script and make it executable
COPY infra/docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

# Copy Poetry configuration files
COPY pyproject.toml .

# Set Poetry to not create virtual environments for global dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Set entrypoint to the custom script
ENTRYPOINT ["./entrypoint.sh"]
