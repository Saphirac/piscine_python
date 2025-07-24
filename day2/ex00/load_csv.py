import pandas as pd


def load(path: str) -> pd.DataFrame:
    pd.set_option("display.show_dimensions", False)

    mydata = pd.read_csv(path, index_col=0)
    # if mydata.empty() :
    #     print("No path, bad format...wtv")
    #     return None
    print("Loading dataset of dimensions", mydata.shape, mydata)

    return mydata


