# Virtual-Glass-TryOn
TryGlass is a hybrid 3D virtual try-on system that allows users to see how eyeglasses would look on their face in real-time using their webcam. It combines the power of Python + Flask with Three.js and MediaPipe to render and align 3D glasses to the user's eyes using face landmark detection.
🔍 Key Features
🧠 Face Landmark Detection with MediaPipe (Python)

🎥 Live Webcam Feed served via Flask backend

🕶️ 3D Glasses Overlay rendered using Three.js and GLTFLoader

🎯 Real-time Alignment of glasses with face/eyes

💻 Frontend-Backend Hybrid Architecture (Python + JavaScript)

🔄 Smooth Tracking without external libraries like AR.js or Unity

🚀 Tech Stack
Frontend: HTML, CSS, JavaScript, Three.js

Backend: Python, Flask

Computer Vision: MediaPipe Face Mesh (for facial landmarks)

3D Model: .glb format (glasses), rendered with GLTFLoader

Video Streaming: Flask route serving MJPEG webcam frames
