# iso

docker-compose -f docker-compose.elastic-stack.yml up -d
fabio@fabio-VJF155F11X-B0311B:~/Documents/GitHub/iso$ docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
WARNING: Owner of file [/usr/share/elasticsearch/config/users] used to be [root], but now is [elasticsearch]
WARNING: Owner of file [/usr/share/elasticsearch/config/users_roles] used to be [root], but now is [elasticsearch]
eyJ2ZXIiOiI4LjEyLjEiLCJhZHIiOlsiMTkyLjE2OC45Ni4yOjkyMDAiXSwiZmdyIjoiMWZiY2ZjNDY5NGIzNDIzMWQyZTNhMjk3ZmNkOGJjOGFiMzg3YWM2NWNjN2UxMGZkNWRkNDZiMzhjNTlkNDUxOCIsImtleSI6InFvNEp2bzBCUEdETHhJNGZWbHZOOnJITEVFajZkU2kyeWJkOW9TaHM4WGcifQ==
fabio@fabio-VJF155F11X-B0311B:~/Documents/GitHub/iso$ docker exec -it kib01 bin/kibana-verification-code
Kibana is currently running with legacy OpenSSL providers enabled! For details and instructions on how to disable see https://www.elastic.co/guide/en/kibana/8.12/production.html#openssl-legacy-provider
Your verification code is:  103 277 
fabio@fabio-VJF155F11X-B0311B:~/Documents/GitHub/iso$ 