from piston import Steem
from piston import account


def auth(login="vgolos5", password="qwerty12345"):
    steem_instance_ = Steem(node="wss://ws.testnet3.golos.io", rpcuser=login, rpcpassword=password)
    user_ = account.Account(account_name=login, steem_instance=steem_instance_)
    return user_


auth()