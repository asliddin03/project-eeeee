#!/bin/bash

ARGUMENT_LIST=(
  "input_folder"
  "extension"
  "backup_folder"
  "backup_archive_name"
)


# read arguments
opts=$(getopt \
  --longoptions "$(printf "%s:," "${ARGUMENT_LIST[@]}")" \
  --name "$(basename "$0")" \
  --options "" \
  -- "$@"
)

eval set --$opts

while [[ $# -gt 0 ]]; do
  case "$1" in
    --input_folder)
      input_folder=$2
      shift 2
      ;;

    --extension)
      extension=$2
      shift 2
      ;;

    --backup_folder)
      backup_folder=$2
      shift 2
      ;;

    --backup_archive_name)
      backup_archive_name=$2
      shift 2
      ;;


    *)
      break
      ;;
  esac
done

mkdir -p $backup_folder
find "$input_folder" -name "*.$extension" -print0 | 
while IFS= read -r -d '' file; do
    cp --backup=numbered "$file" "$backup_folder"
done 

tar czf "$backup_archive_name" "$backup_folder"
echo "done"
