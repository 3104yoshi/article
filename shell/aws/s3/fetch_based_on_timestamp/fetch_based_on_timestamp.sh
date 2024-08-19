#!/bin/bash

# Designated date
TARGET_DATE=$1

# Use awk to filter the table and extract file names
# It's unnecessary to set values with FS and OFS in BEGIN statement because they are default values. 
output=$(awk -v target="$TARGET_DATE" '
BEGIN { FS=" "; }
{
  datetime = $1 " " $2;
  if (datetime > target && NF == 4) {
    print $4;
  }
}' | xargs -I {} echo --include "\"{}\"")

# Print the concatenated string
output="aws s3 cp [s3location] . $output --exclude \"*\""

echo $output
