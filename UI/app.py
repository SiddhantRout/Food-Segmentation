import gradio as gr
from assets.css import css
from helper import get_random_images, process_image, disable_btn_fn, enable_btn_fn
from PIL import Image

# Path to images directory
sample_image_path = r"D:\Projects\CDS\Capstone Project\UECFOOD100\processed_for_yolo\train\images"
images_to_load = 4

image_input_dialog = gr.Image(type="pil", label="Upload or select an image", elem_classes=["image-input"], container=False)
image_output_dialog = gr.Image(type="pil", label="Output Image", elem_classes=["image-output"], container=False)

with gr.Blocks(css=css) as demo:
    tabs = gr.Tabs()
    def change_tab(id):
        return tabs.update(selected=id)

    tab_names = ['Landing Page', 'Select or Upload Image', 'Output']
    with tabs:
        # with gr.TabItem(tab_names[0], id=0):
        #     gr.Markdown("# Welcome to Food Segmentation App!")
        #     gr.Markdown("This app allows you to upload an image of food and see the segmentation results.")
        #     landing_to_upload_button = gr.Button("Upload Image", variant="primary")

        with gr.TabItem(tab_names[1], id=1) as upload_tab:
            gr.Markdown("## Upload or Select an Image")

            # Option to upload an image
            with gr.Column(elem_id="image_input_wrapper"):
                image_input_dialog.render()

            # Initializing invisible gallery
            sample_images_gallery = gr.Gallery(visible=False)
            load_button = gr.Button("Load Sample Images")
            shuffle_button = gr.Button("Change Sample Images", visible=False)

            # Load sample images and display gallery
            def load_sample_images():
                # global sample_images
                sample_images = get_random_images(sample_image_path, images_to_load)
                return (
                    load_button.update(visible=False),
                    shuffle_button.update(visible=True),
                    sample_images_gallery.update(value=sample_images, visible=True, label="Sample Images", 
                                                 columns=4, height='1')
                )
            load_button.click(disable_btn_fn, None, load_button) \
                .then(load_sample_images, outputs=[load_button, shuffle_button, sample_images_gallery]) \
                .then(enable_btn_fn, None, load_button)

            # Shuffle and display new sample images
            def shuffle_images():
                # global sample_images
                sample_images = get_random_images(sample_image_path, images_to_load)
                return sample_images
            shuffle_button.click(disable_btn_fn, None, shuffle_button) \
                .then(shuffle_images, outputs=sample_images_gallery) \
                .then(enable_btn_fn, None, shuffle_button)

            # When a gallery image is selected, set it to the input image
            def update_input_image(selected_image: gr.SelectData):
                # print(selected_image.value)
                # return Image.open(sample_images[selected_image.index])
                return Image.open(selected_image.value[0].split('=')[-1])
            sample_images_gallery.select(update_input_image, inputs=None, outputs=image_input_dialog)

            # Start image processing
            process_button = gr.Button("Process Image", variant="primary")
            # def process_image(input_image):
            #     return [gr.update(value=input_image), gr.update(selected=2)]
            process_button.click(disable_btn_fn, None, process_button) \
                .then(process_image, inputs=image_input_dialog, outputs=[image_output_dialog, tabs]) \
                .then(enable_btn_fn, None, process_button)

        with gr.TabItem(tab_names[2], id=2) as output_tab:
            gr.Markdown("## Segmentation Result")
            with gr.Column(elem_id="image_output_wrapper"):
                image_output_dialog.render()
    
# Launch the Gradio interface
demo.launch() # share=True