#/bin/bash

kubectl delete -f ingress.yaml
kubectl apply -f ingress.yaml
