
docker network rm mynetw

docker network create mynetw

docker  network  ls

docker run -d --name broker -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://broker:9092 -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@broker:9093 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 -e KAFKA_NUM_PARTITIONS=3 --network mynetw apache/kafka:latest


docker run --name mongodb  --network=mynetw -p 27017:27017 -d mongodb/mongodb-community-server:latest

docker build -t image_retriever:v3 -f Retriever/Dockerfile .

docker run --name con_retriever_5  --network=mynetw -d image_retriever:v3

docker build -t image_preprocessor:v4 -f Preprocessor/Dockerfile .

docker run --name con_preprocessor_v4  --network=mynetw -d image_preprocessor:v4

docker build -t image_enricher:v11 -f Enricher/Dockerfile .

docker run --name con_enricher_v11  --network=mynetw -d image_enricher:v11

docker build -t image_data_persister:v4 -f DataPersister/Dockerfile .

docker run --name con_data_persister_v4  --network=mynetw -d image_data_persister:v4

docker build -t image_data_retrivieal:v12 -f DataRetrieval/Dockerfile .

docker run --name con_data_retrivieal_v12  -p 8000:8000 --network=mynetw -d image_data_retrivieal:v12
