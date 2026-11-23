FROM python:3.12-slim
WORKDIR /app
COPY greeter.py .
EXPOSE 8080
CMD ["python", "-u", "greeter.py"]
