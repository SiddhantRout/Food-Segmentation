import gradio as gr
import random
import os
from css import css

# Path to your images directory
image_path = r"D:\Projects\CDS\Capstone Project\UECFOOD100\processed_for_yolo\train\images"  # Replace with your actual path

# Function to get 5 random image file paths from the dataset
def get_random_images():
    image_files = [os.path.join(image_path, f) for f in os.listdir(image_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return random.sample(image_files, 5)

# Function to handle the image processing (for now, we just return the input image)
def process_image(image):
    return image

# Gradio components
image_input = gr.Image(type="filepath", label="Upload or select an image", elem_id="image_input", container=False)
image_output = gr.Image(type="filepath", label="Output Image", elem_id="image_output", container=False)

# Gradio interface setup
with gr.Blocks(css=css) as demo:
    gr.Markdown("# Food Segmentation", elem_id="header", elem_classes=["centered-title"])

    with gr.Row():
        with gr.Column(scale=2):  # Image input takes up 2/3 of the row
            image_input.render()

        with gr.Column(scale=1):  # Sample images and shuffle button take up 1/3 of the row
            # Display 5 random images as thumbnails
            images = get_random_images()
            gallery = gr.Gallery(images, visible=True, label="Or select a sample image").style(
                columns=[5],  # Display in 5 columns
                object_fit="contain",
                height="auto",
                elem_classes=["gallery-container"]
            )

            # Function to update the gallery with new random images
            def shuffle_images():
                global images
                images = get_random_images()
                return images

            shuffle_button = gr.Button("Shuffle Sample Images")
            shuffled_images = shuffle_button.click(shuffle_images, outputs=gallery)

            # When a gallery image is selected, set it to the input image
            def update_input_image(selected_image: gr.SelectData):
                return images[selected_image.index]

            gallery.select(update_input_image, inputs=None, outputs=image_input)

    # Submit button in its own row for full width
    submit_button = gr.Button("Submit")
    submit_button.style(full_width=True)
    submit_button.click(process_image, inputs=image_input, outputs=image_output)

    with gr.Row():
        with gr.Column(scale=2):  # Output image takes up 2/3 of the row
            image_output.render()

# Launch the Gradio interface
demo.launch()
