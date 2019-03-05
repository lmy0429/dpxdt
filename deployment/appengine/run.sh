#!/bin/bash

gcloud \
    --project=dpxdt-local \
    preview app run \
    --host localhost:80 \
    "$@" \
    combined_vm.yaml
