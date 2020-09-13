RUN useradd -m -s /bin/bash -d /opt/app --uid $UID --gid $GID --groups sudo app
RUN echo "app:secret" | chpasswd

WORKDIR /opt/app/app
USER app
