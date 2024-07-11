# JBI100 - New York City Airbnb Open Data Visualization

## Prerequisites

To serve this project locally, create a virtual environment with `python=3.8.15` with necessary dependencies
as are listed in `requirements.txt`.

```shell
# create environment 
conda create -n env python=3.8.15
# activate environment
conda activate env
# install packages
pip install -r requirements.txt
```

And kick off the server with the following command:

```shell
python app.py \
  -p 8050 \
  -H "127.0.0.1" \
  -n
```

## Docker Deployment

The project is also available as a Docker image. 

```shell
# pull the image
docker pull ghcr.io/gitkeniwo/nyc-airbnb-visualization:latest

# run the image
docker run \
  -it \
  --rm \
  -p 8050:8050 \
  --name nyc-airbnb-visualization \
  ghcr.io/gitkeniwo/nyc-airbnb-visualization:latest \
  -p 8050 \
  -n
```

And the application will be available at `http://localhost:8050`.

