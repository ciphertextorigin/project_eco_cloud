#!/bin/bash

echo "Creating the various  k8s"
minikube addons enable ingress


echo "flask deployment and services"

kubectl apply -f deployment.yaml
kubectl apply service.yaml
kubectl apply -f nginx-service.yaml