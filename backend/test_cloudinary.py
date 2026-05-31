import cloudinary
import cloudinary.uploader
import asyncio
from dotenv import load_dotenv
import os

load_dotenv(".env.local")

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

def test_upload():
    try:
        # Create a dummy text file to upload as raw, or image
        with open("dummy.txt", "w") as f:
            f.write("hello world")
            
        result = cloudinary.uploader.upload(
            "dummy.txt",
            folder="groupmatch/avatar",
            resource_type="auto"
        )
        print("Upload successful!", result.get("secure_url"))
    except Exception as e:
        print("Upload failed:", e)

if __name__ == "__main__":
    test_upload()
