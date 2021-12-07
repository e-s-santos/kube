#/bin/bash
docker build . -t essantos70/emsantos70:v2_front

kubectl delete -f k_deployment_front.yaml
kubectl delete -f k_hpa_front-deprecated.yaml
kubectl delete -f k_nodePort_service.yaml

kubectl apply -f k_deployment_front.yaml
kubectl apply -f k_hpa_front-deprecated.yaml
kubectl apply -f k_nodePort_service.yaml
