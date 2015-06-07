FROM python
MAINTAINER Martin Thoma <info@martin-thoma.de>

RUN cd /
RUN git clone https://github.com/MartinThoma/write-math-py.git
RUN cd write-math-py
RUN pip install -r requirements.txt
env PATH /write-math-py:$PATH

EXPOSE 5000

CMD ["/write-math-py/main.py"]