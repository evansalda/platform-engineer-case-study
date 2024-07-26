FROM python:3.12.4

RUN adduser developer
USER developer
WORKDIR /home/developer

COPY --chown=developer:developer links_extractor.py ./

ENTRYPOINT ["python", "./links_extractor.py"]