from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever


def generate_response(query):
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    input_ids = tokenizer(query, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, num_return_sequences=1, num_beams=5)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response