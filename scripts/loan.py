from brownie import Flashloan, accounts, config, network, interface
from scripts.utils import get_account

MINIMUM_FLASHLOAN_WAVAX_BALANCE = 200000000000000000  # 0.2 WAVAX
SNOWTRACE_TX_URL = "https://testnet.snowtrace.io/tx/{}"


def main():
    acct = get_account()
    print(network.show_active())
    flashloan = Flashloan[len(Flashloan) - 1]
    token = interface.Iwavax(
        config["networks"][network.show_active()]["wavax"])
    print(token)
    if token.balanceOf(flashloan) < MINIMUM_FLASHLOAN_WAVAX_BALANCE:
        print("Funding Flashloan contract with WAVAX...")
        token.transferFrom({"from": acct}, flashloan,
                           MINIMUM_FLASHLOAN_WAVAX_BALANCE)
    print("Executing Flashloan...")
    print("token.balanceOf(flashloan): ", token.balanceOf(flashloan))
    tx = flashloan.flashloan(token, {"from": acct})
    print("View your tx here: " + SNOWTRACE_TX_URL.format(tx.txid))
    flashloan.withdraw(token, {"from": acct})
    print("token.balanceOf(flashloan): ", token.balanceOf(flashloan))

    return flashloan
