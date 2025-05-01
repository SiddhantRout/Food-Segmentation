import random
import os
import gradio as gr
import torch
from PIL import Image
from torchvision import transforms
from ultralytics import YOLO

def disable_btn_fn():
    return gr.Button(interactive=False)
def enable_btn_fn():
    return gr.Button(interactive=True)

# Function to get 5 random image file paths from the dataset
def get_random_images(sample_image_path, images_to_load):
    image_files = [os.path.join(sample_image_path, f) for f in os.listdir(sample_image_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return random.sample(image_files, images_to_load)

# Loads the 
def load_model(model_name):
    model_path = os.path.join("models", model_name)
    model = YOLO(model_path)
    return model

def get_annotated_dish_name(input_image):
    # Loading and predicting using the model
    model = load_model("ingr_detection.pt")
    results = model(input_image)

    boxes = results[0].boxes 
    class_ids = boxes.cls.int().tolist()
    label_names = [model.names[cid] for cid in class_ids]
    # print('Predicted Label: ', label_names)

    annotated_img = results[0].plot()  # Annotated numpy image
    annotated_pil = Image.fromarray(annotated_img[:, :, ::-1]).resize(input_image.size)  # Convert BGR to RGB
    return label_names, annotated_pil

# Function to handle the image processing (for now, we just return the input image)
def process_image(input_image):
    predicted_labels, annotated_image = get_annotated_dish_name(input_image)
    return [gr.update(value=annotated_image), gr.update(selected=2)]