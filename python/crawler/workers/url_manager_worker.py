# -------------------------
# title: 
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
import pymongo
import logging


def logger_config():
    logging.basicConfig(filename='logs/url_manager_worker.log', level=logging.DEBUG)
    return logging.getLogger(__name__)


MONGO_CONFIG = {'host': 'mongo', 'port': 27017, 'database': 'wiki', 'collection': 'urls'}
client = pymongo.MongoClient(MONGO_CONFIG['host'], MONGO_CONFIG['port'])
urls = client.wiki.urls
urls.create_index('url', unique=True)


def rabbit_queue_send(queue, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=body)
    connection.close()


def rabbit_queue_receive(queue, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=body)
    channel.start_consuming()


def hash_generator(url):
    return hashlib.sha256(url).hexdigest()


def url_manager(ch, method, properties, body):
    url = body.decode('utf-8')
    found = urls.find_one({'url': url})
    if not found:
        urls.insert_one({'url': url, 'hash': hash_generator(body)})
        logger.debug(f"url {url} filtered.")
        ch.basic_publish(exchange='', routing_key='filtered_urls', body=url)
        logger.info(f"published url_manager {url} to filtered_urls queue.")
    else:
        logger.warning(f"url {url} already exists.")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    logger.debug("ack manager received.")


def main():
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    rabbit_queue_send(queue='filtered_urls', body=url)
    rabbit_queue_receive(queue='unfiltered_urls', body=url_manager)


if __name__ == '__main__':
    os.makedirs('logs', exist_ok=True)
    logger = logger_config()
    main()
