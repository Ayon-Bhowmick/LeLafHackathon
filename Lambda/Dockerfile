FROM public.ecr.aws/lambda/python:3.10

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    groff \
    less \
    && pip3 install --upgrade pip \
    && apt-get clean

RUN pip3 --no-cache-dir install --upgrade redis

CMD ["/bin/bash"]
