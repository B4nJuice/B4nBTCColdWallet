from .wallet_manager import WalletManager
from .wallet import Wallet

if __name__ == "__main__":
    wallet_man = WalletManager()
    wallet: Wallet = wallet_man.init_new_wallet()

    print(wallet.phrase)

    btc_price = wallet_man.get_bitcoin_price()
    usd_price = btc_price.get("usd")
    eur_price = btc_price.get("eur")

    print(f"Balance: {wallet_man.get_balance(wallet) * usd_price}$")

    print(f"BTC Price: {usd_price}$ | {eur_price}€")