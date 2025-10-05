# 1. Use an official Python base image
FROM python:3.10

# 2. Set working directory
WORKDIR /app

# 3. Copy all files into the container
COPY . .

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Run the script
CMD ["python", "app.py"]
