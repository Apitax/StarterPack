# This file builds Apitax core into your application
# This allows you to incorporate custom application code, drivers, and more

# Use the latest version of Apitax
FROM apitax/apitax:3.0.4

# Copy requirements in for driver installs etc.
COPY requirements.txt /tmp/apiax/requirements.txt

# Preform pip install on the requirements file
RUN cd /tmp/apiax && pip install -r requirements.txt --no-cache ; exit 0

# Copy in project, config, and app code
COPY app /app/app

# Remove the tmp folder
RUN rm -rf /tmp/apitax


# EXTRAS AND DRIVER RELATED INSTALLS

# ANSIBLE
#RUN apt-get update && apt-get -y install software-properties-common && apt-add-repository -y ppa:ansible/ansible && apt-get update && apt-get -y install ansible
#RUN pip install ansible --no-cache ; exit 0

