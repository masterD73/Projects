services:
  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - ./dbdata:/data/db
    networks:
      - rabbit

  rabbitmq:
    container_name: rabbitmq
    image: rabbitmq:3-management
    networks:
      - rabbit
    ports:
      - "5672:5672"
      - "15672:15672"

networks:
  rabbit:

