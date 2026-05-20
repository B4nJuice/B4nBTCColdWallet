class WalletCreationError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(f"Wallet creation error: {message}")