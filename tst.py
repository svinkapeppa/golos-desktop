from piston import Steem


def auth():
    steem = Steem(node='wss://ws.testnet3.golos.io', rpcuser='ekhlyzov', rpcpassword='P5KBaPy7XurbVwCK1CUSKDNVGVVrh29xbvXQuYczjYNbdvcw2KYK')
    account_info = steem.info()
    print(account_info)