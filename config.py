
Configuration for the AI Chatbot.
Customize model, lengths, etc., h

# Hugging Face model (DialoGPT-small for quick start; upgrade to 'medium' for better responses)
MODEL_NAME = "microsoft/DialoGPT-small"

# Generation parameters
MAX_LENGTH = 1000  # Max tokens for response generation
HISTORY_LENGTH = 1024  # Max history tokens to retain context

# Other settings
TEMPERATURE = 0.7  # Creativity level (0.5-1.0)
TOP_K = 50  # For sampling diversity
