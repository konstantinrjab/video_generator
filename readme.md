```shell script
docker build --tag vg app
docker run -u $(id -u ${USER}):$(id -g ${USER}) -v ${PWD}/app/:/app vg
```