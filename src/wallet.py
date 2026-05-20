from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39SeedGenerator,
    Bip84,
    Bip84Coins,
    Bip44Changes,
)
from .utils.logger import Logger
from .utils.errors import WalletCreationError

class Wallet:
    def __init__(
                self,
                phrase: str | None = None,
            ):

        if phrase:
            self.init_from_phrase(phrase)
        else:
            self.create_new_wallet()

        self.init_wallet()
        
        Logger.log_info(f"Wallet successfully initialized ({self.address})")

    def create_new_wallet(self) -> None:
        self.phrase: str = Bip39MnemonicGenerator().FromWordsNumber(24)
        Logger.log_info(f"Wallet phrase successfully created.")
        

    def init_from_phrase(self, phrase: str) -> None:
        self.phrase: str = phrase

    def init_wallet(self) -> None:
        self.seed_bytes: bytes = Bip39SeedGenerator(self.phrase).Generate()
        self.wallet: Bip84 = Bip84.FromSeed(self.seed_bytes, Bip84Coins.BITCOIN)

        if not Wallet:
            raise WalletCreationError("Error during wallet creation.")

        self.account = self.wallet.Purpose().Coin().Account(0).Change(
                Bip44Changes.CHAIN_EXT
            ).AddressIndex(0)

        if not self.account:
            raise WalletCreationError("Error during account creation.")

        self.private_key: str = self.account.PrivateKey().ToWif()
        self.address: str = self.account.PublicKey().ToAddress()
