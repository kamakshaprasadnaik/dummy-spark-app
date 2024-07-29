FROM apache/spark:latest
ENV SPARK_HOME=/opt/spark
ENV PATH="${SPARK_HOME}/bin:${PATH}"
WORKDIR /opt/spark/app
COPY ./app.py /opt/spark/app/app.py
COPY ./__init__.py /opt/spark/app/__init__.py
COPY ./DataframeGenerator.py /opt/spark/app/DataframeGenerator.py
ENTRYPOINT spark-submit /opt/spark/app/app.py

