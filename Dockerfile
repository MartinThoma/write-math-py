FROM python
MAINTAINER Martin Thoma <info@martin-thoma.de>

RUN cd /
RUN git clone https://github.com/MartinThoma/write-math-py.git
RUN cd write-math-py
env PATH /write-math-py:$PATH

EXPOSE 5000

CMD ["./main.py"]