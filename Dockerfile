FROM python:3.12.4

RUN adduser developer
USER developer
WORKDIR /home/developer

COPY --chown=developer:developer src/links-extractor.py .

ENTRYPOINT ["python", "./links-extractor.py"]