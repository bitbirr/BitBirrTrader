
from solana.rpc.api import Client
from dotenv import load_dotenv
import os

load_dotenv()
client = Client(os.getenv("RPC_ENDPOINT"))
private_key = os.getenv("PRIVATE_KEY")
public_key = os.getenv("PUBLIC_KEY")

def snipe_token(token_address):
    print(f"Sniping {token_address}...")
    tx_id = "mocked_tx_hash_for_" + token_address
    return tx_id
