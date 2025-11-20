from PIL import Image
import numpy as np

IMG_SIZE = (224, 224)

def load_and_preprocess_image(file_obj, target_size=IMG_SIZE):
    """
    Accepts an uploaded file-like object (streamlit UploadedFile or BytesIO) or path.
    Returns numpy array shaped (1, H, W, 3) scaled to [0,1].
    """
    # If file-like (has read), use it directly
    if hasattr(file_obj, "read"):
        file_obj.seek(0)
        img = Image.open(file_obj).convert('RGB')
    else:
        img = Image.open(file_obj).convert('RGB')

    img = img.resize(target_size)
    arr = np.array(img).astype('float32') / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr
