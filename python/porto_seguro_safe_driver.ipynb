# -------------------------
# title: HTML fetcher
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------    
import os
import pika
import hashlib
import logging
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def logger_config():
    logging.basicConfig(filename='logs/url_fetch_worker.log', level=logging.ERROR)
    return logging.getLogger(__name__)


def rabbit_queue_receive(queue, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=body)
    channel.start_consuming()


def hash_generator(url):
    return hashlib.sha256(url).hexdigest()


def html_fetch(ch, method, properties, body):
    logger.error(f"received html_fetch {body}")

    response = session.get(body)
    status_code = response.status_code
    if not 200 <= status_code < 300:
        logger.error(f"error fetching {body} with status code {status_code}")
        return
    with open("files/" + hash_generator(body) + ".html", 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
    ch.declare_queue('htmls', durable=True)
    ch.basic_publish(exchange='', routing_key='htmls', body=response.text,
                     properties=pika.BasicProperties(delivery_mode=2))
    logger.debug(f"published html_fetch {response} to htmls queue.")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    logger.debug("ack received html_fetch")


def main():
    rabbit_queue_receive(queue='filtered_urls', body=html_fetch)


if __name__ == '__main__':
    os.makedirs('files', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=2)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    logger = logger_config()
    main()
