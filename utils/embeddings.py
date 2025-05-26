import numpy as np
from sklearn.metrics import pairwise_distances
from google.genai import types

def measure_degradation(df, client, emb_model_name, print_shape=True):
    """
    Measure semantic degradation using cosine similarity from the original string.
    """
    texts = df['degraded_text'].tolist()
    response = client.models.embed_content(
        model=emb_model_name,
        contents=texts,
        config=types.EmbedContentConfig(task_type='semantic_similarity')
    )
    
    """ get the embeddings as np.array """
    embeddings = np.array([emb.values for emb in response.embeddings])
    if print_shape:
        print(f"> There are {embeddings.shape[0]} embedding vectors of length {embeddings.shape[1]}.")

    """ check if ALL embeddings are normalized; print note if not """
    norms = np.linalg.norm(embeddings, axis=1)
    non_unit_indices = np.where(np.abs(norms - 1.0) > 1e-5)[0]
    if non_unit_indices.size > 0:
        print(f"NOTE: Some embeddings {non_unit_indices} are not of unit length:")
        print(norms)

    """ calculate similarity distance metrics between base text to other texts
        NOTE: these are "DISTANCE" metrics so that cosine metric is 1 minus its value (0=same) """
    cos_sim = pairwise_distances(embeddings[0:1], embeddings, metric='cosine')[0]
    l2_sim = pairwise_distances(embeddings[0:1], embeddings, metric='euclidean')[0]
    l1_sim = pairwise_distances(embeddings[0:1], embeddings, metric='manhattan')[0]

    """ record results in DF """
    df['embeddings'] = embeddings.tolist()
    df['cos_sim'] = cos_sim
    df['l2_sim'] = l2_sim
    df['l1_sim'] = l1_sim

    return df