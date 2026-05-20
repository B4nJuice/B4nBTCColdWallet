from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39SeedGenerator,
    Bip84,
    Bip84Coins,
    Bip44Changes
)
from .utils.logger import Logger


class Wallet:
    def __init__(
                self,
                phrase: str | None = None,
                private_key: str | None = None
            ):

        if phrase:
            self.init_from_phrase(phrase)
        elif private_key:
            self.init_from_private_key(private_key)
        else:
            self.create_new_wallet()

        if self.account:
            self.private_key = self.account.PrivateKey().ToWif()
            self.address = self.account.PublicKey().ToAddress()
        
        Logger.log_info(f"Wallet created ({self.address})")

    def create_new_wallet(self) -> None:
        self.phrase: str = Bip39MnemonicGenerator().FromWordsNumber(24)
        self.seed_bytes: bytes = Bip39SeedGenerator(self.phrase).Generate()
        self.wallet: Bip84 = Bip84.FromSeed(self.seed_bytes, Bip84Coins.BITCOIN)

        self.account = self.wallet.Purpose().Coin().Account(0).Change(
                Bip44Changes.CHAIN_EXT
            ).AddressIndex(0)

    def init_from_phrase(self, phrase: str) -> None:
        self.phrase: str = phrase
        self.seed_bytes: bytes = Bip39SeedGenerator(phrase).Generate()
        self.wallet: Bip84 = Bip84.FromSeed(slef.seed_bytes, Bip84Coins.BITCOIN)

        self.account = self.wallet.Purpose().Coin().Account(0).Change(
                Bip44Changes.CHAIN_EXT
            ).AddressIndex(0)

    def init_from_private_key(self, private_key : str) -> None:
        ...
