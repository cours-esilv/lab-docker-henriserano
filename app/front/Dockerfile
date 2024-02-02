FROM nginx:alpine

COPY index.html ./index.html
COPY style.css ./style.css
COPY entrypoint.sh ./entrypoint.sh

RUN chmod +x ./entrypoint.sh

# Lancer Nginx en mode foreground
CMD ["nginx", "-g", "daemon off;"]
