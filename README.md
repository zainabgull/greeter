# Greeter

A tiny Python web page that shows a greeting with a date, built with Python's `http.server` and packaged in Docker.

Build and run:

    docker build -t greeter .
    docker run -d -p 8080:8080 greeter

Then open http://localhost:8080. Or run the published image: `docker run -d -p 8080:8080 /greeter:1.1`
