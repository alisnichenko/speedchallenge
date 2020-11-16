My Take on the Comma AI Programming Challenge
======

TL;DR
-----

My goal is to predict the speed of a car from a video.

- data/train.mp4 is a video of driving containing 20400 frames. Video is shot at 20 fps.
- data/train.txt contains the speed of the car at each frame, one speed on each line.
- data/test.mp4 is a different driving video containing 10798 frames. Video is shot at 20 fps.

Relevant Research
-----
Abbreviations: Imitation Learning (IL), End-to-End (E2E), Forward-Facing Camera (FFC).
- IL, E2E, speed control, FFC - [arxiv paper](https://arxiv.org/pdf/1812.05841.pdf).
- Conditional IL, image segmentation, full autonomy, FFC+ - [arxiv paper](https://arxiv.org/pdf/1912.00177.pdf).
- IL, architecture, speed/angle, FFC - [ieee paper](https://ieeexplore.ieee.org/abstract/document/8833873).

TODOs
-----
The following are out of order, since I am typing up tasks as soon as the pop
up during my research. All of them are subject to change.
- Data processing
    - Resizing (haven't figured out the resolution yet).
    - Applying a mask on Comma's dataset.
    - Regulate brightness.
    - Something else?
- Model architecture
    - CNN with LSTM (proven to be working in relevant research).
    - Custom training loss.
    - Lambda layer (?).
    - tensorflow? keras? pytorch? from scratch?
- Evaluation
    - Source custom data.
    - The best way to split the data provided by comma.
    - Google cloud instance. My laptop is trash.
