FROM python:3.10

RUN apt update \
    && apt upgrade -y \
    && apt install -y npm nodejs lsb-release expect \
    && pip3 install online-judge-tools\
    && npm install -g atcoder-cli \
    && pip3 install flake8 \
    && pip3 install autopep8 \
    && acc config default-task-choice all

COPY login_bk.sh $HOME/login.sh