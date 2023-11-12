FROM public.ecr.aws/lambda/python:3.10

RUN pip3 install --upgrade pip \
    && apt-get clean

RUN pip3 --no-cache-dir install --upgrade redis\
    pip3 --no-cache-dir install --upgrade pyzbar

RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm &&\
    yum makecache &&\
    yum -y install zbar

CMD [ "lambda_function.lambda_handler"]
