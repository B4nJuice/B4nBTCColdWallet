from .wallet_manager import WalletManager
from .wallet import Wallet

if __name__ == "__main__":
    wallet_man = WalletManager()
    wallet: Wallet = wallet_man.init_new_wallet()

    print(wallet.phrase)
    print(f"BTC Price: {wallet_man.get_bitcoin_price()}")