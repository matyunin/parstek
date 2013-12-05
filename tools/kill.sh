#!/bin/bash

BASEDIR=$(dirname $0)/..

kill -9 $(ps -aux | grep uwsgi.*parstek | awk '{print $2}')
rm -rf $BASEDIR/tmp/uwsgi.sock
