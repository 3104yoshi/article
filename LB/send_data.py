import pika
import time


def send_data(data):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=data)
    print(f"Sent {data}")

    connection.close()


if __name__ == '__main__':
    while True:
        data = input("Enter data to send: ")
        send_data(data)
        time.sleep(1)
