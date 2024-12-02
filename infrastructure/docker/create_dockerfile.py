# Script to generate a Dockerfile for a Python application
def create_dockerfile(app_name="my_python_app", python_version="3.9", requirements_file="requirements.txt"):
    dockerfile_content = f"""
    # Use an official Python runtime as a parent image
    FROM python:{python_version}-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any necessary dependencies
    RUN pip install --no-cache-dir -r {requirements_file}

    # Make port 80 available to the world outside this container
    EXPOSE 80

    # Define environment variable
    ENV NAME {app_name}

    # Run app.py when the container launches
    CMD ["python", "app.py"]
    """
    with open("Dockerfile", "w") as file:
        file.write(dockerfile_content.strip())

    print("Dockerfile has been created successfully!")

# Execute the function to create a Dockerfile
create_dockerfile()



##How it works.
# 1. Base Image: The script uses a Python slim image (python:3.9-slim by default).
# 2. Working Directory: Sets /app as the working directory inside the container.
# 3. Copy Files: Copies all files from the host's working directory into the container.
# 4. Install Dependencies: Installs dependencies listed in requirements.txt.
# 5. Expose Ports: Exposes port 80 for the application.
# 6. Command to Run: Assumes the app's entry point is app.py.

# Structure
################
# /my_python_app
# ├── app.py
# ├── requirements.txt
