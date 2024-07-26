FROM jupyter/pyspark-notebook
RUN mkdir apps
COPY ./app.py apps/app.py
COPY ./__init__.py apps/__init__.py
COPY ./DataframeGenerator.py apps/DataframeGenerator.py
ENTRYPOINT spark-submit apps/app.py

