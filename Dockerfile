FROM python
MAINTAINER Martin Thoma <info@martin-thoma.de>

RUN git clone https://github.com/MartinThoma/write-math-py.git
RUN pip install -r /write-math-py/requirements.txt

EXPOSE 5000

CMD ["/write-math-py/main.py"]