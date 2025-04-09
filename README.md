# Full-Stack Deployment with Docker Swarm

This is a Full-Stack application deployed using Docker Swarm.  

⚠️ **Security Notice:** This setup uses default credentials and is intended for development or internal testing environments.  
For production use, you should:

- Replace all default passwords and secrets.
- Configure secure authentication (e.g., LDAP, OAuth2, or SSO).
- Enable TLS/SSL for all services handling sensitive data.
- Harden exposed services (e.g., Kong, pgAdmin, Redis, RabbitMQ) by limiting access and enforcing auth.
- Review firewall and network rules to restrict access.

Make sure to audit, monitor, and follow DevSecOps best practices before deploying to any public or production environment.

---

## Overview
- **Frontend**: Angular served by Nginx
- **Backend**: Node.js (Express)
- **Database**: PostgreSQL + pgAdmin
- **Message Queue**: Redis, RabbitMQ
- **API Gateway**: Kong
- **Monitoring**: Prometheus + Grafana
- **Logging**: Elasticsearch, Kibana, Loki
- **Others**: Additional WIP services in `other/`

## Requirements

- Docker & Docker Compose installed
   - **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
   - **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
   ```bash 
   docker swarm init
- Grafana Loki plugin installed:
  ```bash
  docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

## Setup Instructions

1. Clone the Repository
Start by cloning this repository to your local machine:
```
mkdir [name of directory]
cd [path ...]
git clone <repository-url>
cd <repository-directory>
```
2. Create .env file
```
Include passwords and secrets in the env
example:
   POSTGRES_HOST=postgres-db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=1234
   POSTGRES_DATABASE=fullstack
   PGADMIN_DEFAULT_EMAIL=admin@example.com
   PGADMIN_DEFAULT_PASSWORD=admin
```
⚠️ Again follow DevSecOps best practices before deploying in production environment. Again Security and Security.

3. Build and Deploy the Stack
cd into directory 

```
docker compose up --build -d

```
4. Verify the Services

```
docker ps

```
## Architecture

Architecture Overview
---------------------
``` 
[ Nginx ]
   │
   └──→ Serves [ Angular Frontend ] {USER}
   │
   └──→ Serves [ Express Backend ] {Dev team}


[ Angular Frontend ]
   │
   └──→ Makes API requests to → [ Kong API Gateway ]
                                      │
                                      └──→ Routes to → [ Node.js Backend (Express) ]
                                                        │
                                                        ├──→ Connects to [ PostgreSQL (Database) ]
                                                        ├──→ Uses [ Redis (Cache) ]
                                                        └──→ Sends/Receives jobs from [ RabbitMQ (Message Queue) ]

[ Monitoring ]
   ├──→ Prometheus (metrics scraping)
   └──→ Grafana (visual dashboards)

[ Logging ]
   ├──→ Loki (container logs collection)
   ├──→ Elasticsearch (log storage and search)
   └──→ Kibana (log visualization)
```
---

Folder Structure
---------------------
```
.
├── backend/
│   └── Dockerfile
│   └── README.md
├── frontend/
│   └── Dockerfile
│   └── README.md
├── database/
│   └── README.md
├── frontdoor/
│   └── Dockerfile
│   └── README.md
├── monitor/
│   └── Dockerfile
│   └── README.md
│   └── prometheus/
│        └── prometheus.yml
├── other/
│   └── Dockerfile
│   └── README.md
├── docker-compose.yml
└── README.md
└── .env
```
## Services

Access Services
---------------
```
Frontend        -> http://localhost
Backend API     -> http://localhost:3000
Kong Admin API  -> http://localhost:8001
pgAdmin         -> http://localhost:5050
Redis           -> redis://localhost:6379
RabbitMQ UI     -> http://localhost:15672
Prometheus      -> http://localhost:9090
Grafana         -> http://localhost:3000
Kibana          -> http://localhost:5601
```
## Usage

``` docker-compose up --build ```

### Build

### Running unit tests
To run the unit tests for the backend service, navigate to the backend directory and use the following command:
```
docker-compose exec backend_fullstack npm test
```
For the frontend, you can run:
```
docker-compose exec frontend_fullstack npm test

```
### Running end-to-end tests
End-to-end tests can be run using a framework like Cypress or Protractor. 
Run end-to-end tests for the frontend by navigating to the frontend/ directory and running:

```
docker-compose exec frontend_fullstack npm run e2e
```
## Diagrams 

In progress 

## Monitoring & Logging

```
docker logs <container-name>
```
## Troubleshooting

If you encounter issues, here are some troubleshooting tips:

1. Service Not Starting:
   - Check logs with ``` docker logs <container-name>. ```
   - Verify that all services in docker-compose.yml are correctly defined.
2. Port Conflicts:
   - Ensure that no other services are using the ports required by your containers (e.g., localhost:3000 for the backend).
3. Environment Variables:
   - Ensure your .env file contains the correct values, especially for sensitive services like the database and API gateway.
4. Permission Issues:
   - Check if Docker has the required permissions to run containers and access resources on your machine.
5. If None of the Above Work: 
   - Contact me on Linkedin or if you're looking to discuss job opportunities for me, feel free to reach out through the same channels.



## License :oncoming_police_car:
    Copyright 2023 Idriss Kacou

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.