#/bin/bash

kubectl delete -f k_deployment_mysql.yaml
kubectl apply -f k_deployment_mysql.yaml


kubectl delete -f k_configmap_general.yaml
kubectl apply -f k_configmap_general.yaml

