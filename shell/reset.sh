docker-compose down
docker rm -f $(docker ps -q -f status=exited)
docker volume rm $(docker volume ls -qf dangling=true)
