from transformers import pipeline
import sys,os
sys.path.append('.')
from Train.predict import load_model, predict_ml, get_config_gradio, process_text
import gradio as gr

# ner_pipeline = pipeline("ner")
#
examples = [
    ["on april first i need a ticket from tacoma to san jose departing before 7 am", "English"],
    ['tôi muốn tìm một chuyến bay từ đà nẵng đến phú quốc và có một trạm dừng ở cam ranh', 'Vietnamese'],
]

def ner(text, language):
    lines = process_text(text)
    config = get_config_gradio(language=language)
    output, _ = predict_ml(lines, config)
    print(output)
    return {"text": text, "entities": output}

demo = gr.Interface(fn = ner,
             inputs = [gr.Textbox(placeholder="Enter sentence here..."),
                      gr.Radio(["English", "Vietnamese"], label="Language", info="Choose the language of your input")],
             outputs = gr.HighlightedText(),
             examples=examples)

demo.launch(debug = True)



# demo = gr.Interface(ner,
#              gr.Textbox(placeholder="Enter sentence here..."),
#              gr.HighlightedText(),
#              examples=examples)
#
# demo.launch()