
# -- BUILD THE COMMON BASIS STAGE
# -- x--------------------------------x --
# Define the basic image, that we will name "base"
FROM debian:bookworm-slim AS base

# Define the working folser
WORKDIR /app

# Update all package within the container 
# AND update the SSL certificats (UV dependency)
# AND clean the app cash 
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install UV copying the elements from UV server
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 


# UV CONFIGURATION
# -- x---------x --
# Force Python files to be compiled into BYTECODE
ENV UV_COMPILE_BYTECODE=1
#
ENV UV_LINK_MODE=copy
# Download Python when necessary
ENV UV_PYTHON_DOWNLOAD=auto
# -- x---------x --

# -- x--------------------------------x --





# -- BUILD THE BACKEND STAGE
# -- x--------------------------------x --
# Create a new stage for the backend configuration
FROM base AS backend

# Copy the UV required file into the project root
COPY backend/pyproject.toml backend/uv.lock ./

# Install dependencies / libraries
RUN uv sync --frozen --no-install-project --no-dev

# Copy backend content into the project root
COPY backend/ .

# Copy the model into the project to the indicated path
COPY artifacts/flight_price_model.joblib /app/artifacts/flight_price_model.joblib

# RUN the API
CMD ["uv", "run", "uvicorn", "main:app"]
# -- x--------------------------------x --



    # -- BUILD THE FRONTEND STAGE
# -- x--------------------------------x --
# Create a new stage for the backend configuration
FROM base AS frontend

# Copy the UV required file into the project root
COPY backend/pyproject.toml backend/uv.lock ./

# Install dependencies / libraries
RUN uv sync --frozen --no-install-project --no-dev

# Copy backend content into the project root
COPY frontend/ .

# RUN the API frontend Streamlit
CMD ["uv", "run", "streamlit", "run", "main.py"]
# -- x--------------------------------x --