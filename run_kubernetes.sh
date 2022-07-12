#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# This is your Docker ID/path
dockerpath="mshallom/mldocker:latest"

# Run the Docker Hub container with kubernetes
kubectl create deploy mldocker --image=$dockerpath

# List kubernetes pods
kubectl get pods

# Forward the container port to a host
kubectl port-forward pod/$(echo $(kubectl get pods) | awk -F ' ' '{print $6}') --address 0.0.0.0 8000:80
