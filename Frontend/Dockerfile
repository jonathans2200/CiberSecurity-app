FROM node:20-alpine

# Crear directorio de la aplicación
WORKDIR /app

# Copiar archivos de configuración y dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el código fuente
COPY . .

# Exponer puerto 3000
EXPOSE 3000

# Comando para iniciar la aplicación en puerto 3000
CMD ["npx", "vite", "--port", "3000", "--host", "0.0.0.0"]