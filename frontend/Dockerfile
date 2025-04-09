FROM node:20-slim

# Set the working directory inside the container
WORKDIR /frontend

# Install required system dependencies
RUN apt-get update && apt-get install -y git make

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

RUN npm install -g @angular/cli
# Install dependencies
# RUN npm install
RUN npm install --legacy-peer-deps
ARG API_URL
ENV REACT_APP_API_URL=$API_URL

# Copy the rest of the Angular app
COPY . .

# Build the application
# RUN npm run build

EXPOSE 4200

# Build the Angular app for production
# RUN npm run build --prod
CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]

