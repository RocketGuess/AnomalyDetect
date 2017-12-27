docker_build:
	docker build . -t anomaly-detection

docker_up:
	docker run -p 5858:5858 anomaly-detection

docker_clear:
	docker rm $(docker ps -a -q) && \
	docker rmi $(docker images -q)
