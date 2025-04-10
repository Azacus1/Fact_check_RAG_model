
# Fact-Checked News Generation with RAG Model

This project implements a fact-checked news generation system using the Retrieval-Augmented Generation (RAG) model from Hugging Face's transformers library. The system processes user queries to generate accurate, fact-checked news articles.

## Project Structure

The project is organized as follows:

FactCheckedNews/ 
│  ├── model/ 
|  │ 
|  ├── init.py 
|  └── generate_response.py # Function to generate responses │ 
├── webapp/ 
|   ├── init.py 
|   ├── app.py # Flask application 
|   └── templates/ 
|   ├── index.html # Homepage template
|   └── result.html # Result display template
└── README.md # This file


## Setup Instructions

### Prerequisites

Ensure that you have Python and pip installed on your system. If Python is not installed, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions.

### Installation

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://yourrepositorylink.com/FactCheckedNews.git
   cd FactCheckedNews
2. Install Dependencies

pip install -r requirements.txt

3. Running the Application
Set Environment Variables

If running from a non-standard Python installation or encountering module path issues, you might need to set the PYTHONPATH:
set PYTHONPATH=C:\path\to\FactCheckedNews

4. Start the Flask Application

Navigate to the project root directory and run:

python -m webapp.app
