# Reviewer: Alexander Volkovich.
FROM python:3.12-slim AS builder 

WORKDIR /app 

COPY requirements.txt . 

RUN pip install --user --no-cache-dir -r requirements.txt 

RUN mkdir templates

FROM python:3.12-slim 

WORKDIR /app 

COPY --from=builder /root/.local /root/.local 
#COPY /templates/index.html /templates/index.html
#COPY /api_code.py /api_code.py
#COPY /weather.py /weather.py
COPY . .

ENV PATH=/root/.local/bin:$PATH 
ENV FLASK_APP=weather.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000 

CMD ["flask", "run"]
