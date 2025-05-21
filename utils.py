
import pandas as pd
from datetime import datetime

def log_transaction(token, tx_id):
    log_data = {
        "time": datetime.utcnow().isoformat(),
        "token": token,
        "tx_id": tx_id
    }
    try:
        df = pd.read_csv("logs/tx_log.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=log_data.keys())
    df = pd.concat([df, pd.DataFrame([log_data])], ignore_index=True)
    df.to_csv("logs/tx_log.csv", index=False)
