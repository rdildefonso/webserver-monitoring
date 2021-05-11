# webserver-monitoring

Proof-of-concept implementation of automated email alerts via docker healthchecks.

## Prerequisites

* Git
* Docker or Docker Desktop

## Setting-up

### Repository
```
git clone https://github.com/rdildefonso/webserver-monitoring.git
```

### Environment
```
vim .env
```

The application itself would run with no extra configurations, however there are some placeholder defaults specifically for SMTP functionality that needs to be set to facilitate the actual email sending. These variables are the ff:
* HEALTHCHECK_ALERT_SMTP_SERVER - target SMTP server, can be IP or domain
* HEALTHCHECK_ALERT_SMTP_PORT - port for SMTP service
* HEALTHCHECK_ALERT_SMTP_USERNAME - authentication username for SMTP service
* HEALTHCHECK_ALERT_SMTP_PASSWORD - authentication password for SMTP service
* HEALTHCHECK_ALERT_SENDER - email address to show as sender
* HEALTHCHECK_ALERT_RECEPIENTS - email address of alert recepients

Define these variables in the .env file as <variable>=<value>

## Running
```
docker-compose up
```

## Defaults
HEALTHCHECK_URL=http://127.0.0.1:5000/healthcheck - a different route is defined to monitor the service availability of the application. Different route as healthcheck is preferred over running healthchecks against a real application route so that it will be easier to filter-out healthchecks on the application logs. This can be set to http://127.0.0.1:5000/error to force a 504 status code, and thus an email sending trigger.
HEALTHCHECK_ALERT_SMTP_SERVER=localhost
HEALTHCHECK_ALERT_SMTP_SERVER=587
HEALTHCHECK_ALERT_SMTP_USERNAME=admin
HEALTHCHECK_ALERT_SMTP_PASSWORD=admin
HEALTHCHECK_ALERT_SENDER=admin@thisfish.co - a theoretical admin email for domain thisfish.co, as best practice only use organizational domains against domains that you have SMTP credentials for
HEALTHCHECK_ALERT_RECEPIENTS=app_support@thisfish.co - a theoretical group email for domain thisfish.co. This can also be set to comma-separated recipients.
