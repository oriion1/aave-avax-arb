from brownie import Flashloan, accounts, config, network
from scripts.utils import get_account


def deploy():
    acct = get_account()
    flashloan = Flashloan.deploy(
        config["networks"][network.show_active()]["aave_lending_pool"],
        {"from": acct},
    )
    return flashloan


def main():
    return deploy()
