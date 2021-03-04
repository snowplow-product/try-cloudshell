#!/bin/bash

set -e

PURPLE='\033[1;35m'
NO_COLOR='\033[0m' # No Color

echo -e "\n${PURPLE}Deploying your Try Snowplow pipeline...${NO_COLOR}\n"

gcloud config set project "${PROJECT_ID}"

gcloud services enable deploymentmanager.googleapis.com sqladmin.googleapis.com

gcloud deployment-manager deployments create "${DEPLOYMENT_NAME}" \
  --template=./lib/template.py  \
  --properties="license-key:${LICENSE_KEY},database-user:${DATABASE_USER},database-password:${DATABASE_PASSWORD}"

echo -e "\n${PURPLE}Success!!${NO_COLOR}\n"
