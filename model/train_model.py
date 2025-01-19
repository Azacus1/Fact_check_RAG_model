from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever

def train_model():
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact", use_dummy_dataset=True)

    # Assuming some training logic here
    model.retriever = retriever
    # Save model after training
    model.save_pretrained("model/rag_model")

def generate_response(query):
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    input_ids = tokenizer(query, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, num_return_sequences=1, num_beams=5)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    train_model()
    query = "What is AIAGent?"
    generate_response(query)
