 # 🎭 Facial Expression Recognition

Welcome to my cool project where I use some AI magic to recognize facial expressions in real-time! Using OpenCV and DeepFace, this project detects faces and shows you what emotion you're rocking at the moment. It's like having a mirror that reads your mind... well, kinda.

## 🚀 Getting Started

### 1. **Clone the repo**:
```bash
git clone https://github.com/manishpatil55/facial-expression-recognition.git
cd facial-expression-recognition
```

### 2. **Install the goods**:
```bash
pip install -r requirements.txt
```

You’ll need:
- OpenCV (`cv2`)
- DeepFace

### 3. **Plug in your webcam** and make sure it’s ready to capture your epic reactions.

## 🎥 How to Run It

1. **Fire up the script**:
```bash
python main.py
```

2. **Your webcam feed will pop up** with your face highlighted in green. The script will guess your emotion and show it on the screen. Wanna see if it gets your mood right?

3. **Press `q` to quit** whenever you're done.

## 🗂 Project Breakdown

```plaintext
facial-expression-recognition/
│
├── main.py               # The brains of the operation
├── requirements.txt      # All the stuff you need to install
└── README.md             # You're looking at it!
```

## 🧠 What’s Going On Here?

- **Face Detector**: OpenCV is on face patrol, scanning the webcam feed for any mugs to analyze.
  
- **Emotion Detector**: DeepFace steps in to figure out if you’re happy, sad, or just feeling meh.

- **Showtime**: The emotion and a snazzy rectangle around your face show up on the screen.

## 😎 Results

Here are the emotions our little AI friend can detect:
- Happy 😊
- Sad 😢
- Angry 😡
- Surprise 😲
- Fear 😨
- Disgust 😖
- Neutral 😐

## 👾 Wanna Contribute?

Fork this bad boy, make your tweaks, and hit me up with a pull request. All the help is welcome, and I'd love to see what you come up with!

## 📜 License

MIT License – basically, do what you want with it!

---
