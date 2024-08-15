#!/bin/bash

# Designated date
TARGET_DATE=$1

# Use awk to filter the table and extract file names
awk -v target="$TARGET_DATE" '
BEGIN { FS=" "; OFS="\n"; }
{
  datetime = $1 " " $2;
  if (datetime > target && NF == 4) {
    print $4;
  }
}'