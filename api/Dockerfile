# Use the official Python image that includes necessary tools
FROM python:3.10

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# FastText might require special handling if it's not in PyPI
# For the .whl file, you'd need to copy it into the Docker image and then install
# COPY fasttext-0.9.2-cp310-cp310-win_amd64.whl .
# RUN pip install fasttext-0.9.2-cp310-cp310-win_amd64.whl

# Install FastText directly from GitHub
RUN pip install git+https://github.com/facebookresearch/fastText.git

# Copy your application code to the container (make sure you include the model directory)
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
