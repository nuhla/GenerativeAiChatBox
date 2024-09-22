import os 
import PyPDF2
import traceback 
import json

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_file =PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_file.pages:
                text+= page.extract_text()
            return text
        
        except Exception as e:
            raise Exception("Error reding the pdf file")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "Unsupported File Formate only pdf and text are allowed "
        )


def get_table_data(quize_str):
    try:
        quize_dic= json.load(quize_str)
        quize_table_data = []


        for key, value in quize_dic.items():
            mcq=value["mcq"]
            options=" || ".join(
              [  f"{option}-> {option_value}" for option, option_value in value["options"].items()]
            )

            correct = value["correct"]
            quize_table_data.append({"MCQ":mcq, "Choices":options, "correct":correct})
        return quize_table_data
    

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False