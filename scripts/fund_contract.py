from brownie import accounts, config, network, interface
from scripts.utils import get_account


def main():
    """
    Runs the get_weth function to get WETH
    """
    get_token()


def get_token():
    acct = get_account()
    token = interface.Iwavax(
        config["networks"][network.show_active()]["wavax"])
    tx = token.deposit({"from": acct, "value": 100000000000000000})
    print("Received 0.2 WAVAX")
    return tx
