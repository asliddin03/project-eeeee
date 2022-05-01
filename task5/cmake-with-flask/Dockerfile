FROM ubuntu:latest
FROM gcc:latest


WORKDIR /opt/techprog
COPY . .

RUN apt-get update && \
apt-get install -y cmake && \
apt-get install -y g++ && \
apt-get install -y python3 python3-pip && \
python3 -m pip install flask && \
useradd tp2022user && \
cmake . && \
make
USER tp2022user
EXPOSE 8898 
#ENTRYPOINT ["python"]
CMD ["python3", "app.py", "--port", "8898", "--host", "0.0.0.0"]
