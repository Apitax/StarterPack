# This file builds Apitax core into your application
# This allows you to incorporate custom application code, drivers, and more

# Use the latest version of Apitax
#FROM shawnclake/apitax:latest
FROM apitax:latest

# Copy requirements in for driver installs etc.
COPY requirements.txt /tmp/apiax/requirements.txt

# Preform pip install on the requirements file
RUN cd /tmp/apiax && pip install -r requirements.txt ; exit 0

# Copy in project, config, and app code
COPY project.py /app/project.py
COPY config.txt /app/config.txt
COPY app /app/app

# Remove the tmp folder
RUN rm -rf /tmp/apitax
