- Type your messages; end with "quit" or "exit" to stop.
- First run downloads the ~500MB model (one-time).

4. **Customize**:
- Edit `config.py` to change the model (e.g., try "microsoft/DialoGPT-medium" for longer responses).
- Add web interface: See `extensions/web_example.py` (create this file with Flask code if needed).

## Architecture
- **chatbot.py**: Main entry point; handles the conversation loop.
- **config.py**: Model and session settings.
- **utils.py**: Input validation and response generation helpers.
- Powered by Hugging Face Transformers for state-of-the-art NLP.

## Requirements
- Python 3.8+
- See `requirements.txt` for libraries.

## Extending the Project
- **Web Version**: Integrate with Flask/Streamlit. Example:
```python
from flask import Flask, request, jsonify
# Import your chatbot logic here
app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat():
   user_input = request.json['message']
   response = generate_response(user_input)  # From utils.py
   return jsonify({'response': response})
if __name__ == '__main__':
   app.run(debug=True)
