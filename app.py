from flask import Flask, render_template, Response, jsonify, send_from_directory
import cv2
import mediapipe as mp

app = Flask(__name__, static_folder='static')
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False)

cap = cv2.VideoCapture(0)

# Store latest landmark coordinates
latest_landmarks = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def gen_frames():
        global latest_landmarks
        while True:
            success, frame = cap.read()
            if not success:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(frame_rgb)

            if results.multi_face_landmarks:
                h, w, _ = frame.shape
                face_landmarks = results.multi_face_landmarks[0]  # first face only

                # Selected landmark indices
                keypoints = {
                    1: 'nose_tip',
                    33: 'left_eye_outer',
                    263: 'right_eye_outer'
                }

                coords = {}
                for idx, label in keypoints.items():
                    lm = face_landmarks.landmark[idx]
                    x, y = int(lm.x * w), int(lm.y * h)
                    coords[label] = {'x': x, 'y': y}
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                latest_landmarks = coords

            # Convert frame to bytes
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/landmarks')
def landmarks():
    global latest_landmarks
    if latest_landmarks:
        return jsonify(latest_landmarks)
    else:
        return jsonify({})


if __name__ == '__main__':
    app.run(debug=True, port=5050)
