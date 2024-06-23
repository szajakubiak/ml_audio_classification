# ml_audio_classification
 Audio classification using machine learning

## Goal
Record audio samples and their labels and use them to train ML model using TensorFlow.

## Methods
Sound samples are recorded with respective labels using Python script, which reads serial data from [Arduino Nano RP2040 Connect](https://docs.arduino.cc/hardware/nano-rp2040-connect) board. Scripts sends a command to the Arduino to start sound registration and waits for the incoming data. 1 kHz sine wave generated using Audacity was used to verify that sound recording works as intended. TensorFlow ML model is trained in Jupyter notebook.

## Setup
To run TensorFlow you need Linux OS. I recommend using Ubuntu or Debian. If you don't have a Linux PC you can install Ubuntu on Windows using WSL - just go to the Microsoft Store and search for Ubuntu. You should also be able to use Raspberry Pi with Raspberry Pi OS, but I haven't tested that.

### Install required tools
``` bash
sudo apt install python3 python3-pip python3-venv git
```

### Create Python virtual environment and activate it
``` bash
python3 -m venv mlaudio
source mlaudio/bin/activate
```

### Clone repository
``` bash
git clone https://github.com/szajakubiak/ml_audio_classification.git
```

### Install requirements
``` bash
cd ml_audio_classification
pip install -r requirements.txt
```

### Run Jupyter Lab
``` bash
jupyter lab --no-browser
```
You can skip *--no-browser* if you are using PC with Linux installed as a main OS. In such case web browser will be opened with Jupyter Lab tab. If you are on a virtual Linux machine it's better to start web browser on your main system (Windows in my case) and paste in the adress bar link which you will get in the terminal window starting with *localhost:8888/lab* or *127.0.0.1:8888/lab*. Remember to copy the full link with the access token.

## Links
[TinyML tutorial on audio classification](https://blog.tensorflow.org/2021/09/TinyML-Audio-for-everyone.html)

[Talking to an Arduino over Serial with Python](https://seanboe.github.io/blog/python-serial-with-arduino)

## TODO
* Handle case when COM port was not found
* Move request and incoming data parsing into function
