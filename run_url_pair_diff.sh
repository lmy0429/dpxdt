#!/bin/bash

./dpxdt/tools/url_pair_diff.py \
    --release_server_prefix=http://localhost:80/api --upload_build_id=1\
    "$@"
