css = """
.gradio-container {
    background-color: transparent !important;
}

.image-input img {
    min-height: 10vh !important; /* Minimum height relative to viewport height */
    width: 100% !important; /* Take full width of its column */
    object-fit: contain; /* Ensure image fits within the bounds */
}

.image-output {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.image-output img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-height: 70vh !important; /* Maximum height relative to viewport height */
    max-width: 80vh !important;  /* Maximum width relative to viewport height (to aim for square) */
    width: auto !important;
    height: auto !important;
}

.gallery-container { /* Target the gallery container */
    max-height: 10vh; /* Limit the height of the gallery */
    overflow-y: auto; /* Add scroll if more height is needed */
}

.gallery-item { /* Target individual items in the gallery */
    object-fit: contain;
    height: auto !important; /* Let the height adjust based on content within the limited container */
}
"""

# """
# .gradio-container {
#     background-color: transparent !important;
# }

# .image_input {
#     min-height: 40vh !important;
#     width: 100% !important;
#     object-fit: contain;
# }

# .image_output {
#     display: block;
#     margin-left: auto;
#     margin-right: auto;
# }

# #gallery {
#     display: flex; /* Enable flexbox for wrapping */
#     flex-wrap: wrap; /* Allow items to wrap to the next line */
#     gap: 5px; /* Optional: Add some spacing between items */
#     max-height: 50vh; /* Adjust as needed */
#     overflow-y: auto; /* Add scroll if content exceeds max height */
# }

# .gallery-item {
#     width: auto !important; /* Let item width be determined by content */
#     height: auto !important;
#     flex-grow: 1; /* Distribute remaining space */
#     flex-basis: calc(20% - 5px); /* Adjust for desired number of items per row and gap */
#     object-fit: contain;
#     border: 1px solid #ccc; /* Optional: Add a border for visual separation */
# }
# """

# .gradio-container {
#     background-color: transparent !important;
# }

# #image_input {
#     heigh: 150%;
# }

# #image_output {
#     display: block;
#     margin-left: auto;
#     margin-right: auto;
#     width: 40%;
# }