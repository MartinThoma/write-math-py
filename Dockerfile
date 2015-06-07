FROM python
MAINTAINER Martin Thoma <info@martin-thoma.de>

ADD . /write-math-py
RUN pip install -r /write-math-py/requirements.txt

EXPOSE 5000

CMD ["/write-math-py/main.py"]