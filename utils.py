"""
Utility functions for the AI Chatbot.
Handles model loading, response generation, and input cleaning.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_NAME, MAX_LENGTH, TEMPERATURE, TOP_K
import torch

def load_model():
    """
    Load the DialoGPT model and tokenizer.
    Downloads on first run.
    """
    try:
        print("Loading AI model... (This may take a moment on first run.)")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        
        # Fix for GPT-2 tokenizer
        tokenizer.pad_token = tokenizer.eos_token
        
        print("Model loaded successfully! 🚀")
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Ensure you have internet and required libraries installed.")
        return None, None

def generate_response(model, tokenizer, input_ids, max_length=MAX_LENGTH):
    """
    Generate a response using the model.
    """
    with torch.no_grad():
        out = model.generate(
            input_ids,
            max_length=max_length,
            temperature=TEMPERATURE,
            top_k=TOP_K,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            repetition_penalty=1.1  # Avoid repetition
        )
    return out

def clean_input(text):
    """
    Basic input cleaning (remove extra spaces, etc.).
    """
    return ' '.join(text.split()).lower() if text else ""
