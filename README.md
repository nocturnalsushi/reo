## Rio (Real-time Interactive Omnibot)
Rio is an interactive language learning chatbot based on llama3 model using [Groq](https://console.groq.com/docs/quickstart). 

## Features
- Multilingual support
- Context-aware conversation
- Fun facts about languages
- Interactive learning experience

## Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.x
- pip (Python package installer)
- API key from [here](https://console.groq.com/keys)

### Installation
1. Clone the repository:

   ```sh
   git clone https://github.com/nocturnalsushi/rio.git
   cd rio

2. Install the required packages:

    ```sh
    pip install -r requirements.txt

3. Set up environmental variable:
   - Create a `.env` file in the same directory as your `rio.py` file
   - Replace `your_api_key` with your actual API key that was obtained earlier and paste this in the `.env` file.
   
      ```
       GROQ_API_KEY=your_groq_api_key_here
      ```

4. Open rio.py and have a happy learning session!
