ARG VARIANT="3.10-bullseye"
ARG NODE_VERSION="none"

FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV TZ=America/Sao_Paulo 
COPY scripts .
COPY *requirements.txt ./

RUN sh install-req.sh
