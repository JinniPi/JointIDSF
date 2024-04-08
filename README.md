## The implement of Joint Intent Detection and Slot Filling
This is implement of JointIDSF model. I modified based on the offical code and deploy an Google extention and Gradio.
I do experiment on PhoATIS [Vietnamese] dataset and ATIS [English] dataset. My results are shown in the report file "Tasks-report-Trang-Nguyen.pdf". This project is for the NLP class project, just for research. 

## Model installation, training and evaluation

### Installation
- Python version >= 3.6
- PyTorch version >= 1.4.0

```
    git clone https://github.com/JinniPi/JointIDSF.git
    cd JointIDSF/
    pip3 install -r requirements.txt
```

### Training and Evaluation
Run the following bash files to train and evaluate:
```
    scripts/run_jointIDSF_PhoBERTencoder.sh
```

## Deploy API

After training, the model file will be saved into the checkpoint folder. To run the app you can choose Google extension [app.py] or Gradio [app1.py] By the way, to have good insight, I suggest choosing the Gradio option.

## Acknowledgement

My code is based on the unofficial implementation of the JointIDSF paper, from GitHub https://github.com/VinAIResearch/JointIDSF/tree/main

