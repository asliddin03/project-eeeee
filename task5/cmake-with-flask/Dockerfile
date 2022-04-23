FROM ubuntu:latest
FROM gcc:latest


WORKDIR /opt/techprog
COPY . .

RUN apt-get update
RUN apt-get install -y cmake
RUN apt-get install -y g++
RUN useradd tp2022user
RUN cmake .
RUN make
USER tp2022user
