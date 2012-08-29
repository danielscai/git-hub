#!/usr/bin/env python 

import pika 

def callback(ch,method,properties,body):
  print "[x]  Received %r" % (body,)

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='hello')
print '[*] Waring for message. To exit press CTRL+C'
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()

#connection.close()
