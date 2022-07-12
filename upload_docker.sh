#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

dockerpath="mshallom/mldocker"

# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag mldocker:latest mshallom/mldocker:latest

# Push image to a docker repository
docker push mshallom/mldocker:latest