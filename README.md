# Cold Call AI
## AI-Powered Cold Call Agent

**Cold Call AI** is an advanced conversational agent specifically designed to act as a virtual cold call agent for making car insurance deals.

This intelligent system combines natural language processing (NLP) and text-to-speech (TTS) technologies to simulate human-like conversations with customers. It engages potential clients, answers their queries, and discusses insurance policies in a tone that is polite, professional, and friendly.

By leveraging cutting-edge AI, Cold Call AI streamlines the sales process, making it easier for businesses to interact with customers effectively while saving time and resources. The system's life-like speech synthesis ensures an engaging and natural user experience.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Screenshots](#screenshots)
6. [Contributors](#contributors)
7. [Contact](#contact)

---

## Features
1. **Cold Call Agent:** Use the system as a virtual agent for cold calls, specifically designed to simulate interactions for car insurance deals. It engages customers by providing scripted responses, answering queries about insurance policies, and discussing plans in a conversational and human-like manner.
2. **Polite, Friendly, and Professional:** The agent speaks in a tone that is polite, friendly, and professional, ensuring a positive customer experience while maintaining the standards of a real human agent.

---

## Technologies Used
### Frontend:
- **HTML5**, **CSS3**, **JavaScript**: For an intuitive and responsive user interface.

### Backend:
- **Flask**: Python web framework to manage server-side logic and API routing.
- **Python**: Core programming language for chatbot logic and text-to-speech integration.

### APIs:
- **Gemini Chatbot API**: Pre-trained model for financial queries.
- **Smallest.ai API**: Converts text into speech using AI-based TTS services.

---

## Installation

### Prerequisites
- Python 3.x
- Required Python libraries

### Install Dependencies
Run the following command to install all necessary packages:
```bash
pip install flask flask-cors python-dotenv requests
```

### Steps to Run the Project
1. Clone the repository name the folder as Cold-Call-AI:
   ```bash
   git clone https://github.com/Archana-K-M/Cold-Call-AI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Cold-Call-AI
   ```
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
4. Install dependencies and unzip the essentials folder:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure `.env` file:
   - Create a `.env` file in the project root.
   - TTS_API_KEY can be generated from https://waves-docs.smallest.ai/waves-api
   - GEMINI_API_KEY can be generated from https://ai.google.dev/gemini-api/docs
   - Add the following keys:
     ```env
     GEMINI_API_KEY=your_gemini_api_key
     TTS_API_KEY=your_tts_api_key    
     ```
6. Run the application:
   ```bash
   flask run
   ```
7. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage
1. **Cold Call Agent:** Use the system as a virtual agent for cold calls, specifically designed to simulate interactions for car insurance deals. It engages customers by providing scripted responses, answering queries about insurance policies, and discussing plans in a conversational and human-like manner.
2. **Polite, Friendly, and Professional:** The agent speaks in a tone that is polite, friendly, and professional, ensuring a positive customer experience while maintaining the standards of a real human agent.

---

## Screenshots
Here are some screenshots of the application:
![image](https://github.com/user-attachments/assets/c6366b72-a6ec-459e-85c2-d51ac259090e)


---

## Contributors
We thank the following people for their contributions to this project:

- **Archana K M** - (https://github.com/Archana-K-M)
- **Anirudhh S** - (https://github.com/rudhhstoic)
- **Devanidharshan** - (https://github.com/Deva399212)
- **Varsha G** - (https://github.com/Varshavishnu)

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## Contact
For any inquiries or feedback, reach out to:

- **Archana K M**  
  **Email**: archanakm297@gmail.com  
  **GitHub**: [Archana-K-M](https://github.com/Archana-K-M)
