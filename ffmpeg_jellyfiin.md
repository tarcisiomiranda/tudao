#!/bin/bash
# chmod 775 folder serie
# https://www.reddit.com/r/jellyfin/comments/wezh4o/ffmpeg_command_for_jellyfin_playable_mkvmp4_format/
SOURCE_DIR="/home/tm/Downloads/Katla_S01.2021_1080p.WEB-DLDUBLADO.5.1.COMANDO.TO/agora/"

for file in "$SOURCE_DIR"/*.mkv; do
    filename=$(basename -- "$file")
    extension="${filename##*.}"
    filename="${filename%.*}"
    output_file="$SOURCE_DIR/$filename.mp4"

    ffmpeg -i "$file" -c:v libx264 -profile:v high -level 4.0 -c:a aac -strict experimental "$output_file"
    echo "Converted $file to $output_file"
done
