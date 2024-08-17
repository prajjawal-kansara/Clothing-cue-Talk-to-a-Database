
# Clothing Cue: Talk to a Database  

This is an end to end LLM project based on Google Palm and Langchain that enables natural language interactions with a MySQL database for a T-shirt store.
This system allows store managers to query inventory, sales, and discount data using everyday language.
User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and
then executing that query on MySQL database. 
Clothing Cue is a T-shirt store where they maintain their inventory, sales and discounts data in MySQL database. A store manager 
will may ask questions such as,
- How many white color Adidas t shirts do we have left in the stock?
- How much sales our store will generate if we can sell all extra-small size t shirts after applying discounts?
The system is intelligent enough to generate accurate queries for given question and execute them on MySQL database.

![clothing_cue](https://github.com/user-attachments/assets/fe63cf78-6fd1-4dc1-9b9b-3fdc1b3189c9)

## Key Features
- Natural Language Processing: Converts user questions into SQL queries
- Intelligent Query Generation: Accurately interprets complex questions about inventory and sales
- Real-time Database Interaction: Executes queries on MySQL database and returns results
- User-friendly Interface: Streamlit-based UI for easy interaction

## Technology Stack
  - LLM: Google Palm
  - Embedding: Hugging Face
  - Frontend: Streamlit
  - Framework: Langchain
  - Vector Store: Chromadb
  - Machine Learning Technique: Few-shot learning
  - Database: MySQL


## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/prajjawal-kansara/Clothing-cue-Talk-to-a-Database.git
```
2.Navigate to the project directory:

```bash
  cd clothing_cue_tshirts
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```
5. For database setup, run database/db_creation_t_shirts.sql in your MySQL workbench

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser where you can ask questions

## Sample Questions
  - How many total t shirts are left in total in stock?
  - How many t-shirts do we have left for Nike in XS size and white color?
  - How much is the total price of the inventory for all S-size t-shirts?
  - How much sales amount will be generated if we sell all small size adidas shirts today after discounts?
  
## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- few_shots.py: Contains few shot prompts
- .env: Configuration file for storing your Google API key.
