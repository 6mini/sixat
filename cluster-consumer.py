from kafka import KafkaConsumer # 패키지

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"] # 통신 할 브로커 리스트 생성
consumer = KafkaConsumer("first-cluster-topic", bootstrap_servers=brokers) # 프로듀서 인스턴스화

for message in consumer: # 컨슈머가 메세지를 받을 때 마다 프린트
  print(message)