## The implement of Joint Intent Detection and Slot Filling
This is implement of JointIDSF model. I modified based on the offical code and deploy an Google extention and Gradio.
I do experiment on PhoATIS [Vietnamese] dataset and ATIS [English] dataset. My results are shown in report file. 

## Model installation, training and evaluation

### Installation
- Python version >= 3.6
- PyTorch version >= 1.4.0

```
    git clone https://github.com/VinAIResearch/JointIDSF.git
    cd JointIDSF/
    pip3 install -r requirements.txt
```

### Training and Evaluation
Run the following bash files to train and evaluation:
```
    scripts/run_jointIDSF_PhoBERTencoder.sh
```

## Deploy API

After training, the model file will save in to checkpoint folder. To run the app you can choose Google extension [aap.py] or Gradio [app1.py] By the way, to have good insight, I suggest to choose Gradio option.

