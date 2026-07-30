# Define the basic image 
FROM debian:bookworm-slim

# Define the working folder
WORKDIR /app

# Update all package within the container AND update the SSL certificats (UV dependency)
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates

# Add environment variables to manage UV parameters
# -- x----------------------x --
# Indicate to UV to ignore libraries listed into "dev dependencies"
ENV UV_NO_DEV=1 
# Force Python files to be compiled into BYTECODE
ENV UV_COMPILE_BYTECODE=1
# Download Python when necessary
ENV UV_PYTHON_DOWNLOAD=auto

# -- x----------------------x --

# Install UV copying the elements from UV server
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

# Copy files required by UV and add them within the current folder
COPY pyproject.toml uv.lock ./

# Create the UV environment using 
# --frozen flag to strictly respect what is within the the uv.lock file
# --no-install-project to ask to not ìnstall the project as it is not here yet
RUN uv sync --frozen --no-install-project


# Copy our project source code
COPY . .
  
# To install the project itself
RUN uv sync --frozen


# RUN a command to check that everything worked well : display UV version
#CMD ["uv", "--version"]
# RUN a command to check that everything worked well : display UV Python version
CMD ["uv", "run", "python", "--version"]