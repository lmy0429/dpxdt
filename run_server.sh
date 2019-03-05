#!/bin/bash

./dpxdt/tools/run_server.py \
    --enable_api_server \
    --reload_code \
    --port=80 \
    --verbose \
    --ignore_auth \
    $@
