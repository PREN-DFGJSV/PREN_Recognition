import cv2

from src.common.ConfigProperties import ConfigProperties

config = ConfigProperties()


class VideoStream:
    
    @staticmethod
    def open_camera():
        cap = cv2.VideoCapture(
            "rtsp://" +
            config.RTSP_USERNAME + ":" + config.RTSP_PASSWORD +
            "@" + config.RTSP_URL +
            "?streamprofile=" + config.RTSP_PROFILE)
        
        if cap is None or not cap.isOpened():
            print("Video-Stream: Error accessing stream ", config.RTSP_IP, flush=True)
            return None
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Video-Stream: Error reading next frame", flush=True)
                break

            cv2.rectangle(frame, config.ROI_UPPER_LEFT, config.ROI_BOTTOM_RIGHT, (100, 50, 200), 5)
            
            cv2.imshow("Video-Stream (close with 'q')", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
