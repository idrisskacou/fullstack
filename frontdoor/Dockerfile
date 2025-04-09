# Use an official Nginx image
FROM nginx:alpine

# Copy custom Nginx config
# COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY html/ /usr/share/nginx/html/


# Ensure log directory exists
RUN mkdir -p /var/log/nginx && chmod -R 777 /var/log/nginx

# Expose logs to Docker
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Expose Nginx port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]


# # docker build --no-cache -t admin .
# # docker run -d -p 8080:80 admin