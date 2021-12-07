#/bin/bash

docker build . -t essantos70/emsantos70:back_v2

kubectl delete -f  k_deployment_back.yaml
kubectl delete -f  k_hpa_service.yaml
kubectl delete -f  k_load_balance_service.yaml
kubectl delete -f  k_configmap_back.yaml

kubectl apply -f  k_deployment_back.yaml
kubectl apply -f  k_hpa_service.yaml
kubectl apply -f  k_load_balance_service.yaml
kubectl apply -f  k_configmap_back.yaml
# k_nodePort_service.yaml

