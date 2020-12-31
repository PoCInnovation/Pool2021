echo Documentation is running on 'http://localhost:8001'
docker run -it --rm -p 8001:80 -v $(pwd)/api/poc-space.yaml:/usr/share/nginx/html/openapi.yaml -e SPEC_URL=openapi.yaml redocly/redoc
