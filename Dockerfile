# Crea un dockerfile que me levante jenkins
FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y python3-pip

USER jenkins
# Exponer el puerto 8080 para Jenkins
EXPOSE 8080
# Comando para iniciar Jenkins
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]
# Ejecutar el comando para iniciar Jenkins
# docker build -t jenkins-python .
# docker run -p 8080:8080 jenkins-python
# docker exec -it <container_id> bash

