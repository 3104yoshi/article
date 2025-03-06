import pika
import time


def send_data(data):
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', credentials))
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
