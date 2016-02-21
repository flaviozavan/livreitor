if [ $# -lt 2 ]; then
  echo "Usage: $0 WARPED_DIR PDF [JPG_QUALITY]"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "$1 is not a directory"
  exit 2
fi

if [ "$3" == "" ]; then
  QUALITY="70%"
else
  QUALITY="$3"
fi

convert "$1/frame_*.png" -compress jpeg -quality "$QUALITY" "$2"
