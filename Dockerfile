FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y python3.12 python3-pip python3-venv && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt
COPY . .
EXPOSE 5000
# Adicionamos o env PYTHONPATH=src para o Gunicorn enxergar os módulos internos
CMD ["python3", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "--env", "PYTHONPATH=src", "src.app:app"]
