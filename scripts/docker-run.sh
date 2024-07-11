docker run \
  -it \
  --rm \
  -p 8050:8050 \
  nyc-airbnb:latest \
  -p 8050 \
  -n

docker run \
  -it \
  --rm \
  -p 8050:8050 \
  --name nyc-airbnb-visualization \
  ghcr.io/gitkeniwo/nyc-airbnb-visualization:latest \
  -p 8050 \
  -n