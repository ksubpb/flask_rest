# Dockerのベースイメージを指定する．
FROM python:3

# 作業ディレクトリを指定する．
WORKDIR /app

# Flask に必要なパッケージを列挙したものをコンテナ内にコピーする．
COPY ./requirements.txt /app

# Flask に必要なパッケージをコンテナ内にインストールする．
RUN    pip install --upgrade pip \
    && pip install -r requirements.txt
