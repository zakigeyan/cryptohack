#!/bin/sh

echo "crypto{y0ur_f1rst_fl4g}"
python great_snakes.py
echo "{\"buy\":\"flag\"}" | nc socket.cryptohack.org 11112
