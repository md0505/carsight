# Carsight - Predictions for predestrian crossing using Particle Swarm Optimization on YOLO object detection data

Using YOLO v2 and the Joing Attention in Autonomous Driving [JAAD](http://data.nvision2.eecs.yorku.ca/JAAD_dataset/), carsight produces predictions of pedestrian crossings from video data. It provides a prediction horizon on a frame basis.
 

## Setup

Pre-process the desired video by converting it to frames (ffmpeg in Julia was used for this project)
Run the conversion python script to copy and convert your frames from PNG to JPG format needed by YOLO v2:
```
python convert_images.py
```

## Running
Run using:
```
] julia
julia> using IJulia
julia> notebook()
```
