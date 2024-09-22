import os
import json
import pandas as pd 
import traceback
from langchain.chat_models import ChatOpenAI
from  dotenv import load_dotenv
from src.mcqgenerator.utils import read_file , get_table_data
from src.mcqgenerator.logger import logging

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.callbacks import get_openai_callback
import PyPDF2
from datetime import datetime

#---------- Load the enviroment vartiable ----------------#
load_dotenv()

#---------- Access the enviroment variable  ----------------#
key = os.getenv("KEY")

llm= ChatOpenAI(openai_api_key = key, model_name = "gtp-3.5-terbu", temperature=.7)

TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your jobe to \
create a quiz of {numbers} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to fornate your respones like RESPONSE_JSON below and use it a guide.
Ensure to make {numbers} MCQs
### RESPONSE_JSON
{response_json}
    
"""


quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "numbers", "subject", "tone", "response_json"],
    template=TEMPLATE
)

quize_chain= LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)


TEMPLATE2 ="""
    You are an expert english grammarian and writer. given a Multiple choice Quiz fro {subject} students.\
    You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity 
    if the quiz is not at per with the conngitive and analytical abilities of the students,\
    update the quiz questions which needs to be changes and change the tone such that it perfectly fits the students .
    Quiz_MCQs:
    {quiz}

    Check from an export English writer of the above quize:
"""

quiz_evaluation_prompt=PromptTemplate(
    input_variables=["subject", "quiz"], template=TEMPLATE2
)

review_Chian = LLMChain(llm=llm, prompt=quiz_evaluation_prompt , output_key="review", verbose=True)


BOOT = SequentialChain(chains=[quize_chain, review_Chian], input_variables=["text", "numbers", "subject", "tone", "response_json"],
                       output_variables=["quiz", "review"],verbose=True)

fil_path="../data.txt"
with open (fil_path, "r") as file:
    text = file.read()

print(text)