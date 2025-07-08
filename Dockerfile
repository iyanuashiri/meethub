FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

LABEL version="1.0.2"

WORKDIR /code


# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./


# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    # --mount=type=bind,source=uv.lock,target=uv.lock \
    # --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project --no-dev

COPY . /code

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev
    
ENV PATH="/code/.venv/bin:$PATH"

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh


ENTRYPOINT ["/code/entrypoint.sh"]
