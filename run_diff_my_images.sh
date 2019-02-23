#!/bin/bash

./dpxdt/tools/diff_my_images.py \
    --release_server_prefix=http://localhost:5000/api \
    "$@"
#windows test cmd
#python2 ./dpxdt/tools/diff_my_images.py --upload_build_id=1 --release_server_prefix=http://localhost:5000/api --release_cut_url=http://example.com/path/to/my/release/tool/for/this/cut --casefile_path=./dpxdt/server/static/upl
#oads/
