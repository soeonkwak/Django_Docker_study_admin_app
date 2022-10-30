import pika  # 이벤트를 보내는데 필요한 패키지

# URL주소는 CloudAMQP에서 계정생성하고 부여 받은 거.
params = pika.URLParameters('amqps://uuyqugbb:koSGNC-lwhlAm83l-uCIDy5g2SGJ5yBj@dingo.rmq.cloudamqp.com/uuyqugbb')

# rabbitMQ로 연결 생성
connection = pika.BlockingConnection(params)

# channel 생성 -> connection의 channel이랑 동일
channel = connection.channel()


# 함수 생성 -> 이 함수 사용해서 products.views 에서 메세징 할 수 있음.
def publish():
    # routing_key: 이벤트를 보내고 싶은 큐? -> admin app에서 뭔가 이벤트가 발생하면 main app으로 메세지 보낼 거니까 'main'
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
