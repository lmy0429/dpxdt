 #!/bin/bash

./dpxdt/tools/run_server.py \
    --enable_queue_workers \
    --release_server_prefix=http://localhost:80/api \
    --queue_server_prefix=http://localhost:80/api/work_queue \
    --verbose \
    "$@"
