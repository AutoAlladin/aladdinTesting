import pika


def send_simple(que_name, body, _durable=True):
    # параметры подключения к шине
    parameters = pika.ConnectionParameters(host='192.168.95.153',
                                           port=5672,
                                           credentials= pika.PlainCredentials(
                                                    'AutoTest',
                                                    '66596659'
                                                )
                                           )
    con_rabbit = None
    try:
        con_rabbit = pika.BlockingConnection(parameters)
        ch = con_rabbit.channel()
        ch.queue_declare(queue=que_name, durable=_durable)

        # кидаем сообщение
        ch.basic_publish(exchange='',
                         routing_key=que_name,
                         body=body)

        print(" [x] Sent " + body)
    finally:
        con_rabbit.close()

