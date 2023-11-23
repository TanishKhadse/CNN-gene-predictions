FROM gcc:latest

COPY . /usr/src/cnn-gene-predictions
WORKDIR /usr/src/cnn-gene-predictions

RUN make

CMD ["./exec"]

LABEL Name=cnn-gene-predictions Version=0.0.1

# WORKDIR /graphs

# docker build -t 




# run multiple containers; nginx, Python, Node, gcc
# Docker compose used to control everything together