# DJAPM - Django Elastic APM
Projeto para estudo da integração Django com Elastic APM para monitoramento de performance de uma API REST.

## Serviços
- Postgres
- Rabbitmq
- ElasticSearch
- Kibana
- Elastic APM

### Iniciar Django Docker Compose
```
docker-compose up -d
```

| IMAGE | COMMAND | STATUS | PORTS | NAMES |
| ----- | ------- | ------ | ----- | ----- |
| postgres:12 | "docker-entrypoint.s…" | Up About an hour | 0.0.0.0:5432->5432/tcp | djapm_postgres_1 |
| rabbitmq:3-management | "docker-entrypoint.s…" | Up About an hour | 4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp, 15671/tcp, 25672/tcp, 0.0.0.0:15672->15672/tcp | djapm_rabbitmq_1 |

### Iniciar APM Docker Compose
```
docker-compose -f apm-docker-compose.yml up -d
```

| IMAGE | COMMAND | STATUS | PORTS | NAMES |
| ----- | ------- | ------ | ----- | ----- |
| docker.elastic.co/elasticsearch/elasticsearch:7.8.1 | "/tini -- /usr/local…" | Up About an hour (healthy) | 0.0.0.0:9200->9200/tcp, 9300/tcp | djapm_elasticsearch_1 |
| docker.elastic.co/kibana/kibana:7.8.1 | "/usr/local/bin/dumb…" | Up About an hour (healthy) | 0.0.0.0:5601->5601/tcp | djapm_kibana_1 |
| docker.elastic.co/apm/apm-server:7.8.1 | "/usr/local/bin/dock…" | Up About an hour (healthy) | 0.0.0.0:8200->8200/tcp | djapm_apm_server_1 |

### Iniciar Django
- Criar virtualenv
- Instalar requisitos
```
pip install -r requirements/dev.txt
```

- Inicar Django
```
./manage.py runserver
```

### Iniciar Celery Worker e Beat
- Iniciar Worker com fila padrão
```
celery worker -A djapm -l INFO
```

- Iniciar Beat com task configurada para uma chamada por minuto
```
celery beat -A djapm -S django -l INFO
```

### Acessar APM
Após exectuar os serviços, acesse o kibana (http://localhost:5601) na aba APM, há um menu para configurar e inciar o monitoramento.

### Scripts
- Popular base de dados de usuários
```
./manage.py runscript populate_db_users
```

- Simular várias requisições de vários usuários
```
./manage.py runscript random_request
```

- Simular várias chamadas de tasks de vários usuários
```
./manage.py runscript random_tasks
```

## Referências

### Elastic APM - Monitoramento de performance de aplicação open source
https://www.elastic.co/pt/apm

### Configurar Elasticsearch com Docker
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker

### Configurar Kibana com Docker
https://www.elastic.co/guide/en/kibana/current/docker.html#docker

### Executar APM Server no Docker
https://www.elastic.co/guide/en/apm/server/7.8/running-on-docker.html#running-on-docker
