stop:
	docker stop `(docker ps -a -q)`
	docker rm `(docker ps -a -q)`
clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -type d -name "__pycache__" -delete