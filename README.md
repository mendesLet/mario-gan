## Mario GAN: Generative Level Design for Mario Bros

A Generative Adversarial Network (GAN) model designed to procedurally generate Super Mario Bros. levels. This model leverages sequential GANs to create cohesive and engaging level layouts with continuous and playable segments.

#### Dataset

In the dataset folder there is a test dataset extracted from the Video Game Level Corpus and processed by github user "shyamsn97" from the [MarioGPT](https://github.com/shyamsn97/mario-gpt/blob/main/mario_gpt/level.py) repository. Use it as reference to run the processing notebook found in the `dataset` directory. The dataset used to train the GAN will be private until further notice.

#### To Do

* [X] Make our own dataset
* [X] Create model architecture
* [ ] Train model with own dataset
* [ ] Create inference function with the sequential results
* [ ] Add playable/pathfinder enviorioment 
