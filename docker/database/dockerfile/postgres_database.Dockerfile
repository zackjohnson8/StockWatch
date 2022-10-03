# Get the 14.5-bullseye postgres image from Docker Hub.
FROM postgres:14.5-bullseye

#ARG POSTGRES_PASSWORD
#COPY use_secret .
#RUN --mount=type=secret,id=postgres_password ./use_secret.sh
