import cloudinary.uploader

async def upload_avatar(file):
    contents = await file.read()
    result = cloudinary.uploader.upload(
        contents,
        folder="groupmatch/avatar"
    )
    return result.get("secure_url")
