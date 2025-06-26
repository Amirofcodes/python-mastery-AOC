############  python-mastery dev image ############
ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

# ─ env hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ─ install uv (fast package manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# ─ non-root user (file permissions match host UID:GID)
ARG USER=dev
ARG UID=1000
ARG GID=1000
RUN groupadd --gid ${GID} ${USER} \
    && useradd  --uid ${UID} --gid ${GID} --create-home --shell /bin/bash ${USER}
WORKDIR /home/${USER}/app
USER ${USER}

# ─ copy project metadata & install deps
COPY --chown=${USER}:${USER} pyproject.toml .
RUN uv pip install -e ".[dev]"

# ─ copy source for live-reload via bind-mount
COPY --chown=${USER}:${USER} . .

# default shell (override in compose / CI)
CMD ["bash"]
