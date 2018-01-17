import pika
import time

parameters = pika.ConnectionParameters(host='192.168.95.153',
                                       port=5672,
                                       credentials=pika.PlainCredentials(
                                           'AutoTest',
                                           '66596659'
                                       )
                                       )
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='delphi_test', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='delphi_test')

channel.start_consuming()