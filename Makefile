docker-image:
	docker build -t embedding-srv:0.1.0 .

docker-run:
	docker run -it --rm \
		-p 8000:8000 \
		--env .env \
		embedding-srv:0.1.0

remove-images:
	docker rmi -f embedding-srv:0.1.0 && docker system prune -f
