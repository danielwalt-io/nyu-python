#!/usr/bin/env bash

LOCATION="us-east4"
PROJECT="dwio-nyu"
REPOSITORY="dwio-nyu-python"

rm -rf build dist ./*egg-info
python3 setup.py sdist bdist_wheel

gcloud artifacts repositories delete ${REPOSITORY} --location=${LOCATION}
gcloud artifacts repositories create ${REPOSITORY} --location=${LOCATION} --repository-format=python
gcloud artifacts repositories add-iam-policy-binding ${REPOSITORY} --location=${LOCATION} --member=allUsers \
--role=roles/artifactregistry.reader

twine upload --repository-url https://${LOCATION}-python.pkg.dev/${PROJECT}/${REPOSITORY}/ dist/*