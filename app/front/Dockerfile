FROM nginx:alpine

WORKDIR /app
COPY . .

RUN chmod +x ./entrypoint.sh

# Lancer Nginx en mode foreground
CMD ["nginx", "-g", "daemon off;"]
