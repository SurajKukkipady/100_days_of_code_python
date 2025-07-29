import os
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from collections import Counter

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    image_url = ""
    if request.method == "POST":
        image = request.files["image"]
        if image:
            # Save uploaded image
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(image_path)
            image_url = "/" + image_path

            # Extract top colors
            colors = get_top_colors(image_path, num_colors=10)

    return render_template("index.html", colors=colors, image_url=image_url)

def get_top_colors(image_path, num_colors=10):
    img = Image.open(image_path)
    img = img.resize((150, 150))  # Resize to speed up processing
    img_np = np.array(img)

    # Flatten to 2D: rows = pixels, cols = RGB
    pixels = img_np.reshape(-1, img_np.shape[-1])

    # Convert to list of tuples (R, G, B)
    pixels = [tuple(pixel[:3]) for pixel in pixels]  # Remove alpha if present

    # Count frequency of each color
    color_counts = Counter(pixels)
    common_colors = color_counts.most_common(num_colors)

    # Convert to HEX
    hex_colors = [{"rgb": rgb, "hex": '#%02x%02x%02x' % rgb} for rgb, count in common_colors]

    return hex_colors

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
