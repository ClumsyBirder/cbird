# 使用官方的 Python 基础镜像
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .

RUN python -m venv venv
RUN /app/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# 第二阶段：应用镜像
FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /app/venv /app/venv

RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata wget vim && \
    rm -rf /var/lib/apt/lists/*

COPY . .
EXPOSE 5000
CMD ["/app/venv/bin/python", "main.py"]