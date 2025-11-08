# =============================
# Etapa 1: Construcción de Angular
# =============================
FROM node:20-alpine AS build

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias primero para aprovechar cache
COPY package*.json ./

# Instalar dependencias (más rápido que npm install)
RUN npm install

# Copiar el resto del código
COPY . .

# Compilar la app Angular (modo producción)
RUN npm run build

# =============================
# Etapa 2: Servir con Nginx
# =============================
FROM nginx:alpine

# Elimina la config por defecto de Nginx
RUN rm -rf /etc/nginx/conf.d/*

# Copiar tu config personalizada
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiar los archivos compilados al directorio de Nginx
COPY --from=build /app/dist/app-angular/browser /usr/share/nginx/html

# Exponer puerto 80
EXPOSE 80

# Comando de inicio
CMD ["nginx", "-g", "daemon off;"]
