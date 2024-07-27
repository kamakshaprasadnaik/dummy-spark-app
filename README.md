# DUMMY-SPARK-APP
This is a dummy spark app that generates dummy data and does some transformations on them. 
# Running the application
## Using kubernetes
If you have a kubernetes cluster running with kubectl you can run the application </br>

    kubectl apply -f Deployment-kube.yaml 

This creates a deployment

## Using Docker
You can run the application by pulling the image from docker.io/kamakshaprasadnaik/dummy-spark-app:\<tag>

[Source Docker link](https://hub.docker.com/r/kamakshaprasadnaik/dummy-spark-app)

    docker run kamakshaprasadnaik/dummy-spark-app:\<tag> 


## Using Spark
If you have a spark cluster configured you can clone the repo and run it

    spark-submit app.py 

# Base Image
It uses jupyter/pyspark-notebook base image which comes configured with everything needed to run the spark jobs. We can try creating a smaller image maybe from python:3.11-slim or apache/spark:\<spark-version>. That could be part of enhancements done for the project. 
