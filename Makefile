#!/bin/bash
repository = portfolio
tag = 0.3.0
platform = linux/amd64,linux/arm64

build:
	poetry export --without-hashes --output requirements.txt
	docker build -t $(repository) .

publish:
	poetry export --without-hashes --output requirements.txt
	docker buildx build --platform $(platform) --push -t docker.robbyte.net/$(repository):$(tag) .