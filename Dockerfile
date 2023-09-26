FROM python

RUN pip install --upgrade pip

RUN groupadd --gid 1000 onvif && \
    useradd --gid 1000 --no-log-init --home-dir /onvif --uid 1000 onvif
WORKDIR /onvif

COPY --chown=onvif:onvif . .
RUN pip install --root-user-action=ignore -r requirements.txt

USER onvif
CMD ["python", "main.py"]