import pandas as pd


def load(path: str) -> pd.DataFrame:
    pd.set_option("display.show_dimensions", False)

    try:
        mydata = pd.read_csv(path, index_col=0)
        return mydata
    except Exception as e:
        print(f"An error occured : {e}")
        return None
