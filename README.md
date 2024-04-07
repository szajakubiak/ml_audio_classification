# ml_audio_classification
 Audio classification using machine learning

## Goal
Record audio samples and their labels and use them to train ML model using TensorFlow.

## Methods
Sound samples are recorded with respective labels using Python script, which reads serial data from [Arduino Nano RP2040 Connect](https://docs.arduino.cc/hardware/nano-rp2040-connect) board. Scripts sends a command to the Arduino to start sound registration and waits for the incoming data. 1 kHz sine wave generated using Audacity was used to verify that sound recording works as intended. TensorFlow ML model is trained in Jupyter notebook.

## Links
[TinyML tutorial on audio classification](https://blog.tensorflow.org/2021/09/TinyML-Audio-for-everyone.html)

[Arduino Nano RP2040 cheat sheet](https://docs.arduino.cc/tutorials/nano-rp2040-connect/rp2040-01-technical-reference)

[Read audio data on Arduino Nano RP2040](https://docs.arduino.cc/tutorials/nano-rp2040-connect/rp2040-microphone-basics)

[Talking to an Arduino over Serial with Python](https://seanboe.github.io/blog/python-serial-with-arduino)

## TODO
* Python - handle case when COM port was not found
* Python - move request and incoming data parsing into function
* Jupyter notebook to train ML model
* Arduino - consider replacing error messages with error codes
* Arduino - collect several values for single measurement from accelerometer
