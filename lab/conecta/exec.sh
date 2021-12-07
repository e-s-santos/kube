#/bin/bash 
docker build . -t essantos70/emsantos70:v1_conecta

kubectl delete -f k_configmap_conecta.yaml
kubectl apply -f k_configmap_conecta.yaml

kubectl delete -f k_cronjob_conecta.yaml
kubectl apply -f k_cronjob_conecta.yaml
