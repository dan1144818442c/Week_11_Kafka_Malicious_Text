
docker build -t  danc12/image_retriever -f Retriever/Dockerfile .

docker push danc12/image_retriever



docker build -t  danc12/image_preprocessor -f Preprocessor/Dockerfile .

docker push danc12/image_preprocessor


docker build -t  danc12/image_enricher -f Enricher/Dockerfile .

docker push danc12/image_enricher


docker build -t  danc12/image_data_persister -f DataPersister/Dockerfile .

docker push danc12/image_data_persister

docker build -t  danc12/image_data_retrivieal -f DataRetrieval/Dockerfile .

docker push danc12/image_data_retrivieal


oc new-app mongodb/mongodb-community-server:latest

oc new-app apache/kafka:latest

oc new-app danc12/image_retriever:latest -e USER=IRGC_NEW -e PASS=iran135 -e DBNAME=IranMalDB

oc new-app danc12/image_preprocessor:latest

oc new-app danc12/image_enricher:latest

oc new-app danc12/image_data_persister:latest

oc new-app danc12/image_data_retrivieal:latest

