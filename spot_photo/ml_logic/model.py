
from sentence_transformers import SentenceTransformer, util
from spot_photo.ml_logic.data import load_data
from PIL import Image
#from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer





# DEF A FUNCTION TO LOAD CAPTIONING MODEL

#def load_captionning_model():
    # model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    # feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    # tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    # return X_pred #CSV WITH CAPTIONING


# DEF A FUNCTION TO LOAD SENTENCE SIMILARITY MODEL
def load_sentence_similarity_model(model_name='all-mpnet-base-v2'):
    # Instanciate Model
    if model_name == 'all-mpnet-base-v2':
        model = SentenceTransformer('all-mpnet-base-v2')
    if model_name == 'clip-ViT-B-32':
        model = SentenceTransformer('clip-ViT-B-32')
    return model

def embedding_query(model, query):
    # Embedding query
    query_embedding = model.encode(query)
    return query_embedding

def compute_similarity(query_embedding, X_pred_embeddings, k=5):
    hits = util.semantic_search(query_embedding, X_pred_embeddings, top_k=k)
    hits_sorted = sorted(hits[0], key = lambda ele: ele['score'], reverse=True)

    # Create list of images result index
    list_of_index = []
    for hit in hits_sorted :
        list_of_index.append(hit['corpus_id'])
    print (list_of_index)
    data = load_data()
    # Create list of images name
    list_of_image_name = []
    for i in list_of_index :
        print(data['image_name'][55])
        image_na = data['image_name'][i*5]
        print(image_na)
        list_of_image_name.append(image_na)

    return list_of_image_name



# DEF A FUNCTION TO LOAD TEXT TO IMAGE MODEL * IF BETTER
