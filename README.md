# Full-Stack Deployment Docker Swarm

A production-ready full-stack application powered by Docker Swarm. 

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


## Architecture

Architecture Overview
---------------------
``` 
[ Nginx ]
   │
   └──→ Serves [ Angular Frontend ]

[ Nginx ]
   │
   └──→ Serves [ Angular Frontend ]

[ Nginx ]
   │
   └──→ Serves [ Express Backend ]

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
## Requirements

- Create a .env file
- Docker & Docker Compose installed
- Grafana Loki plugin installed:
  ```bash
  docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

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

### Running end-to-end tests

## Diagrams 

## Monitoring & Logging

## Troubleshooting

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