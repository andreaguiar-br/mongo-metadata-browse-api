#!/bin/bash
gunicorn --reload --pythonpath ./src -w 4 -b 127.0.0.1:8400 server:app 