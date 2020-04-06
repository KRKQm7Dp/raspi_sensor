nohup ffmpeg -re -f video4linux2 -i /dev/video0 -f flv -c:v h264_omx rtmp://39.107.125.189/myapp/raspi >nohup.out 2>&1 &
