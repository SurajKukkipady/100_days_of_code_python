import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark Application")

        self.image = None  # Original image
        self.watermarked_image = None

        # Upload Button
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        # Canvas for image preview
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        # Watermark Text Entry
        self.text_label = tk.Label(root, text="Watermark Text:")
        self.text_label.pack()

        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.pack(pady=5)

        # Add Watermark Button
        self.add_text_btn = tk.Button(root, text="Add Text Watermark", command=self.add_text_watermark)
        self.add_text_btn.pack(pady=5)

        # Save Image Button
        self.save_btn = tk.Button(root, text="Save Watermarked Image", command=self.save_image)
        self.save_btn.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.image = Image.open(file_path).convert("RGBA")  # Use RGBA for transparency support
            self.display_image(self.image)

    def display_image(self, img):
        img_preview = img.copy()
        img_preview.thumbnail((400, 400))
        self.tk_image = ImageTk.PhotoImage(img_preview)
        self.canvas.delete("all")
        self.canvas.create_image(200, 200, image=self.tk_image)

    def add_text_watermark(self):
        if self.image:
            watermark_text = self.text_entry.get()
            if not watermark_text:
                messagebox.showwarning("Input Error", "Please enter watermark text.")
                return

            img_copy = self.image.copy()
            draw = ImageDraw.Draw(img_copy)

            # Load font safely
            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except IOError:
                font = ImageFont.load_default()
                messagebox.showinfo("Font Info", "Default font loaded. Install Arial.ttf for better results.")

            # Get text size using textbbox
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            width, height = img_copy.size
            x = width - text_width - 10
            y = height - text_height - 10

            # Add semi-transparent watermark
            text_layer = Image.new("RGBA", img_copy.size, (0, 0, 0, 0))
            text_draw = ImageDraw.Draw(text_layer)
            text_draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
            combined = Image.alpha_composite(img_copy, text_layer)

            self.watermarked_image = combined
            self.display_image(combined)
        else:
            messagebox.showerror("Error", "Please upload an image first.")

    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if file_path:
                # Convert to RGB if saving as JPEG (JPEG doesn’t support transparency)
                if os.path.splitext(file_path)[1].lower() in [".jpg", ".jpeg"]:
                    save_image = self.watermarked_image.convert("RGB")
                else:
                    save_image = self.watermarked_image

                save_image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully.")
        else:
            messagebox.showerror("Error", "No watermarked image to save.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
