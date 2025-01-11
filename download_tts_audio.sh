#!/bin/bash

VIDEO_URL=$1

# Get the video title and sanitize it to remove problematic characters
OUTPUT_TITLE=$(yt-dlp --get-title "$VIDEO_URL" | sed 's/[:]/_/g')
OUTPUT_FILE="${OUTPUT_TITLE}.wav"
FORMATTED_FILE="${OUTPUT_TITLE}_formatted.wav"

# Download the audio and convert it to the correct format
yt-dlp -f bestaudio -x --audio-format wav --output "$OUTPUT_FILE" "$VIDEO_URL" \
&& ffmpeg -i "$OUTPUT_FILE" -ar 22050 -ac 1 -sample_fmt s16 "$FORMATTED_FILE"

echo "Formatted file saved as $FORMATTED_FILE"
