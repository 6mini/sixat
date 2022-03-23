from kafka import KafkaProducer # 패키지

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"] # 스트링 값으로 브로커 리스트 저장
topicName = "first-cluster-topic" # 토픽 이름 지정

producer = KafkaProducer(bootstrap_servers = brokers) # 프로듀서를 인스턴스화

producer.send(topicName, b"Hello cluster world") # 토픽을 받아 스트링값을 전송
producer.flush()