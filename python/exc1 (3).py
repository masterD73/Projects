# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ----------------------------
import os
import pika
import logging
from bs4 import BeautifulSoup


def logger_config():
    logging.basicConfig(filename='logs/url_extractor_worker.log', level=logging.DEBUG)
    return logging.getLogger(__name__)


def rabbit_queue_receive(queue, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=body)
    channel.start_consuming()


def url_extractor(ch, method, properties, body):
    html = body.decode()
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.find_all('a', href=True)
    links = {'https://en.wikipedia.org' + element['href'] for element in urls
             if element['href'].startswith('/wiki/') and ':' not in element['href']}
    for link in links:
        ch.basic_publish(exchange='', routing_key='unfiltered_urls', body=link)
        logger.debug(f"published url_extractor {link} to filtered_urls queue.")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    logger.debug("ack received url_extractor")


def main():
    rabbit_queue_receive(queue='htmls', body=url_extractor)


if __name__ == '__main__':
    os.makedirs('logs', exist_ok=True)
    logger = logger_config()
    main()
