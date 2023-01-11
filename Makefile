#!/bin/bash
repository = portfolio
tag = 1.0.0
platform = linux/amd64,linux/arm64

build:
	poetry export --without-hashes --output requirements.txt
	docker build -t $(repository) .

publish:
	poetry export --without-hashes --output requirements.txt
	docker buildx build --platform $(platform) --push -t rdurica/$(repository):$(tag) .