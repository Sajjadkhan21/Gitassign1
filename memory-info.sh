#!/bin/bash

echo "Memory information"

free -h

echo "Summary of memory stats"
top -bn1 | head -5
