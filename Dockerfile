FROM public.ecr.aws/lambda/python:3.12

COPY app.py app.py

COPY wsgi_handler.py wsgi_handler.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


CMD ["wsgi_handler.handler"]
# CMD [ "python", "app.py" ]

