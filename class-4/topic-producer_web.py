import time

from server import channel

QUEUES = [
    {
        "name": "data-lake",
        "routing_key": "logs"
    },
    {
        "name": "data-clean",
        "routing_key": "logs"
    }
]

EVENTS = [
    {
        "routing_key": "a",
        "body": "event 1"
    },
    {
        "routing_key": "b",
        "body": "event 1"
    }
]

#boucle pour parcourir l'ensemble des logs

EXCHANGE_NAME = "topic-exchange-web"

# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')

# create queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['routing_key'])


# publish event
for event in EVENTS:
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=event['routing_key'], body=event['body'])
    time.sleep(2)
    print(f"[x] published event `{event['body']}` in topic `{event['routing_key']}`")



#https://www.rabbitmq.com/tutorials/tutorial-one-python.html