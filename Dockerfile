FROM python:3

WORKDIR /usr/src/app

COPY ./src/requirements.txt ./
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN apt install gunicorn
COPY ./src/. .
# ver como passar a senha de outra forma e mudar o usuário para um específico para o monitor.
ENV SCHEMA_DB=""
CMD [ "./runServer.sh" ]


EXPOSE 8012