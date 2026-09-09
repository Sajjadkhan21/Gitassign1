#!/bin/bash

echo "disk usage(Filesystem)"
df -hT
df -hT
echo -e "\n ==== Block devices ===="
lsblk

echo "done"
