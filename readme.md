# 🌐 Machine Translation with LSTM Neural Networks

A modern web-based language translation application powered by LSTM (Long Short-Term Memory) neural networks. Translate English text to Tamil, French, and Spanish through an elegant, fast API-driven interface.

![Python](https://img.shields.io/badge/python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## ✨ Features

- **Real-time Translation** - Instant English to Tamil/French/Spanish translation
- **Modern UI** - Dark-themed responsive interface with glassmorphism design
- **RESTful API** - FastAPI backend with clean endpoints
- **LSTM Models** - Pre-trained encoder-decoder architecture
- **User-Friendly** - Loading indicators, error messages, keyboard shortcuts (Ctrl+Enter)
- **Lightweight** - No external API dependencies, runs locally

## 🎯 Supported Languages

| From | To |
|------|-----|
| 🇬🇧 English | 🇮🇳 Tamil |
| 🇬🇧 English | 🇫🇷 French |
| 🇬🇧 English | 🇪🇸 Spanish |

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/debanjan-mondal-2005/Machine_Translation.git
cd Machine_Translation

# Create virtual environment (if not exists)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install fastapi uvicorn[standard] python-multipart tensorflow tf-keras numpy joblib dill
```

### Run the Application

```bash
# Start the FastAPI server
uvicorn main:app --reload

# Or use the full path
.venv\Scripts\python.exe -m uvicorn main:app --reload
```

**Access the app:** Open your browser and navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
Machine_Translation/
├── main.py                    # FastAPI application with /translate endpoint
├── eng_tam_model.py          # English → Tamil translation model
├── eng_fre_model.py          # English → French translation model
├── eng_spa_model.py          # English → Spanish translation model
├── fre_eng_model.py          # French → English (placeholder)
├── spa_eng_model.py          # Spanish → English (placeholder)
├── tam_eng_model.py          # Tamil → English (placeholder)
├── Models/                    # Pre-trained LSTM models & tokenizers
│   ├── eng-taencoder.h5      # Tamil encoder model
│   ├── eng-tadecoder.h5      # Tamil decoder model
│   ├── en-frencoder.h5       # French encoder model
│   ├── en-frdecoder.h5       # French decoder model
│   ├── en-spencoder.h5       # Spanish encoder model
│   ├── en-spdecoder.h5       # Spanish decoder model
│   └── *.pkl                 # Tokenizer files (dill-serialized)
├── static/                    # Frontend assets
│   ├── index.html            # Main UI interface
│   ├── style.css             # Dark-themed responsive styling
│   └── script.js             # Client-side translation logic
├── .venv/                     # Python virtual environment
└── README.md                  # This file
```

## 🔧 API Documentation

### Endpoints

#### `GET /`
Returns the main HTML interface.

#### `POST /translate`
Translates text from English to the target language.

**Request:**
```json
{
  "text": "Hello, how are you?",
  "source_lang": "English",
  "target_lang": "Tamil"
}
```

**Response:**
```json
{
  "input": "Hello, how are you?",
  "translation": "வணக்கம், எப்படி இருக்கிறீர்கள்?",
  "source": "English",
  "target": "Tamil"
}
```

**Error Response:**
```json
{
  "error": "Translation from English to Hindi is not supported."
}
```

## 🧠 Model Architecture

The translation system uses a **sequence-to-sequence LSTM encoder-decoder architecture**:

1. **Encoder**: Processes input English text and generates context vectors
2. **Decoder**: Generates target language output token by token
3. **Tokenization**: Custom tokenizers convert text ↔ sequences
4. **Padding**: Sequences padded to fixed lengths for batch processing

**Model Specifications:**
- **Framework**: TensorFlow 2.x with tf-keras (legacy Keras 2)
- **Input Length**: 4-6 tokens (varies by language)
- **Output Length**: 5-9 tokens (varies by language)
- **Training**: Pre-trained on parallel corpus datasets

## 🛠️ Technologies Used

**Backend:**
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [TensorFlow](https://www.tensorflow.org/) - Deep learning framework
- [tf-keras](https://github.com/keras-team/tf-keras) - Legacy Keras 2 for model compatibility

**Frontend:**
- HTML5, CSS3, Vanilla JavaScript
- Responsive design with glassmorphism effects
- Fetch API for async requests

**Machine Learning:**
- LSTM (Long Short-Term Memory) networks
- Encoder-Decoder architecture
- Custom tokenizers with dill serialization

## 📦 Dependencies

```
fastapi>=0.109.0
uvicorn[standard]>=0.27.0
python-multipart>=0.0.9
tensorflow>=2.15.0
tf-keras>=2.15.0
numpy>=1.26.0
joblib>=1.3.2
dill>=0.3.8
```

## 🎨 Screenshots

**Main Interface:**
- Clean, modern dark theme
- Source language: English (fixed)
- Target language: Tamil/French/Spanish selector
- Live translation with loading spinner

**Features:**
- ✅ Real-time error messages
- ✅ Translation results with source/target display
- ✅ Mobile-responsive layout
- ✅ Keyboard shortcuts (Ctrl+Enter)

## 🔮 Future Enhancements

- [ ] Reverse translation (Tamil/French/Spanish → English)
- [ ] Additional languages (Hindi, Bengali, German, etc.)
- [ ] Batch translation support
- [ ] Translation history
- [ ] Model fine-tuning interface
- [ ] Audio input/output (speech-to-text + text-to-speech)
- [ ] API rate limiting and authentication
- [ ] Docker containerization

## 🐛 Known Issues

- Reverse direction models (target → English) not yet implemented
- Model file size (~30MB) - consider model compression
- Limited to short phrases (max 4-6 input tokens)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Debanjan Mondal**
- GitHub: [@debanjan-mondal-2005](https://github.com/debanjan-mondal-2005)

## 🙏 Acknowledgments

- Original LSTM translation model architecture
- TensorFlow and Keras teams
- FastAPI framework developers
- Open-source NLP community

## 📞 Support

For issues, questions, or suggestions:
- Open an [issue](https://github.com/debanjan-mondal-2005/Machine_Translation/issues)
- Contact: [Your Email]

---

**Made with ❤️ using Python, TensorFlow, and FastAPI**
