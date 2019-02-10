FROM python:3-onbuild
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install -U pip
RUN pip install smbus2
RUN pip install requests
RUN pip install wxPython
CMD ["python3","./simple.py"]