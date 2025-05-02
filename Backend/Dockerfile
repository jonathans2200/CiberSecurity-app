# Usa una imagen ligera con Python
FROM python:3.14-rc-alpine3.20
# Establecer variables de entorno para evitar la escritura de archivos .pyc y para que Python no bufferice la salida
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto para FastAPI
EXPOSE 8000

# Comando para correr la aplicación con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
