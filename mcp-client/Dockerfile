# mcp-client/Dockerfile

FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential python3-dev libpq-dev \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY mcp-client/requirements.txt ./requirements-client.txt
COPY mcp-server/requirements.txt ./requirements-server.txt

RUN pip install --no-cache-dir -r requirements-client.txt \
    && pip install --no-cache-dir -r requirements-server.txt

COPY mcp-client/ ./
COPY mcp-server/mcp_server.py ./mcp_server.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]