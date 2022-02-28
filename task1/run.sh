#!/bin/bash

# объявляем список из 4 аргумента
ARGUMENT_LIST=(
  "input_folder"
  "extension"
  "backup_folder"
  "backup_archive_name"
)

# $# - переменная аргументы
# в цикле мы рассмотриваем пока значение $# > 0
while [[ $# -gt 0 ]]; do
  # рaссмотриваем аргумент $1 в switchcase в каждом из случаев заносим значение аргумента $2 в соответствующую переменную 
  # shift сдвигает все аргументы на две позиции в лево
  case "$1" in
    --input_folder)
      input_folder=$2
      shift 2
      ;;

    --extension)
      extension=$2
      shift 2
      ;;

# $
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
# мы ищем все файлы с росширением extension
# print0 что бы функция find ничего не выводила
find "$input_folder" -name "*.$extension" -print0 |
# IFS - форматирует вывод функции find и все отделные названия файлов итарируются в цикле 
while IFS= read -r -d '' file; do
    # cp - копирует файл в папку назначения
    # --backup=numbered - нумирует файл с одинаковую названия
    cp --backup=numbered "$file" "$backup_folder"
done 

tar czf "$backup_archive_name" "$backup_folder"
echo "done"
