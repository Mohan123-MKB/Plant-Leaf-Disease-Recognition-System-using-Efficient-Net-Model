import numpy as np
from .image_processing import load_and_preprocess_image

TOP_K = 3

def get_topk_probs(model, file_obj, k=TOP_K):
    x = load_and_preprocess_image(file_obj)
    preds = model.predict(x)[0]
    topk_idx = preds.argsort()[-k:][::-1]
    return topk_idx, preds

def predict_image_class(model, file_obj, class_indices, k=TOP_K):
    """
    Returns (top1_class_name, top1_score, topk_list)
    topk_list = [{'class': name, 'score': float}, ...]
    class_indices: dict mapping string-index -> class_name
    """
    x = load_and_preprocess_image(file_obj)
    preds = model.predict(x)[0]
    topk_idx = preds.argsort()[-k:][::-1]

    topk = []
    for idx in topk_idx:
        name = class_indices[str(int(idx))]
        topk.append({'class': name, 'score': float(preds[int(idx)])})

    top1 = topk[0]
    return top1['class'], top1['score'], topk
