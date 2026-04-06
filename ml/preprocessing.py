import pandas as pd

def clean_text(text):
    text = text.lower()
    text = text.strip()
    text = text.replace(" _" , "_")
    text = " ".join(text.split())
    return text

def load_and_preprocess_data(path):
    df = pd.read_csv(path)

    # remove NaN
    df = df.fillna("")

    # get symptom columns 
    symptom_cols = df.columns[1:]

    # combine symptoms
    df["symptoms"] = df[symptom_cols].apply(
        lambda row: " ".join(row.values), axis=1
    )

    #  apply cleaning
    df["symptoms"] = df["symptoms"].apply(clean_text)

    # features & labels
    X = df["symptoms"]
    y = df["Disease"]

    return X, y