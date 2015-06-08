#!/usr/bin/env bash
docker build .
newContainerId=`docker images -q | head -1`
docker run -d -p 8080:5000 $newContainerId