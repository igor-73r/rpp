FROM python

WORKDIR /django-project

COPY requirements.txt /django-project
RUN pip install -r requirements.txt

COPY . /django-project

EXPOSE 8000

CMD python ./WebProject/manage.py runserver