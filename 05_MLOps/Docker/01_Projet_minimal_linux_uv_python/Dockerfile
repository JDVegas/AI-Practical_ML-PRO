# Define the basic image 
FROM debian:bookworm-slim

# Define the working folder
WORKDIR /app

# Update all package within the container AND update the SSL certificats (UV dependency)
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates

# Add environment variables to manage UV parameters
# -- x----------------------x --
# Indicate to UV to ignore libraries listed into "dev dependencies"
ENV UV_NO_DEV = 1 
# Force Python files to be compiled into BYTECODE
ENV UV_COMPILE_BYTECODE = 1
# Download Python when necessary
ENV UV_PYTHON_DOWNLOAD = auto

# -- x----------------------x --

# Install UV copying the elements from UV server
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

# Copy the entire project folder content
COPY . . 

# Create the UV environement within the container
# Here the file `.lock` from UV will be used within the container
RUN uv sync --locked


# RUN a command to check that everything worked well : display UV version
CMD ["uv", "--version"]