########  python-mastery dev image (uv + system site-packages)  ########

ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 1️⃣ uv available globally
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir uv

# 2️⃣ non-root user maps host UID/GID
ARG USER=dev
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} ${USER} \
    && useradd  -m -u ${UID} -g ${GID} -s /bin/bash ${USER}

WORKDIR /home/${USER}/app

# 3️⃣ project deps (runtime + dev) straight into system site-packages
COPY pyproject.toml .
RUN uv pip install --system -e ".[dev]"

# give dev ownership of uv cache dir
RUN mkdir -p /home/dev/.cache/uv && chown -R dev:dev /home/dev/.cache

# 4️⃣ copy source and drop to unprivileged user
COPY --chown=${USER}:${USER} . .
USER ${USER}

CMD ["bash"]
