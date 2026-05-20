from bitcoinlib.services.services import Service
from pycoingecko import CoinGeckoAPI

from typing import Any
from .wallet import Wallet

class WalletManager:
    def __init__(self) -> None:
        self.service: Service = Service()
        self.coin_gecko: CoinGeckoAPI = CoinGeckoAPI()

        self.wallets: list[Wallet] = []

    def init_new_wallet(self, kwargs: dict[Any]) -> Wallet:
        new_wallet = Wallet(*kwargs)
        self.wallets.append(new_wallet)

        return new_wallet

    def get_balance(self, wallet: Wallet) -> int:
        return self.service.getbalance(wallet.address)

    def get_bitcoin_price(self, vs_curr: str = "usd") -> float:
        return self.coin_gecko.get_price(
            ids='bitcoin',
            vs_currencies=vs_curr
        )