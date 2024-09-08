#!/bin/sh

false &

wait $!

echo "false command terminated: $?"
