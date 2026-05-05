#Reviewer: Alexander Volkovich.

FROM ubuntu:latest

COPY names.sh /names.sh

RUN chmod +x /names.sh

RUN useradd -Ms /bin/bash hezi

USER hezi

CMD ["/names.sh"]
