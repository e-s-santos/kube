#/bin/bash

#kubectl delete -f k_configmap_general.yaml
#kubectl apply -f k_configmap_general.yaml

kubectl delete -f k_deployment_mysql.yaml
kubectl apply -f k_deployment_mysql.yaml

kubectl create secret generic db-user-pass --from-file=./pass
#kubectl delete -f k_configmap_general.yaml
#kubectl apply -f k_configmap_general.yaml

