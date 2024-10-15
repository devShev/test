#!/bin/sh
cd parse_wb
celery -A parse_wb worker -l INFO