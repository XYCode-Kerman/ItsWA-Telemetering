FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN poetry install

CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "4624", "main:app"]
EXPOSE 4624