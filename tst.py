from piston import Steem
from piston import account


class User:

    def __init__(self, login="vgolos3", password="P5Hu2Vb5N2Gsrp5cWSZp4tHvaJr5cUBtmwEQJs7C6N6oU52E8q7d"):
        self.steem_instance_ = Steem(node="wss://ws.testnet3.golos.io", rpcuser=login, rpcpassword=password)
        self.user_ = account.Account(account_name=login, steem_instance=self.steem_instance_)

    def get_posts(self, limit=10,
                  sort="active",
                  category=None,
                  start=None):
        #list of dicts
        return self.steem_instance_.get_posts(limit=limit, sort=sort, category=category, start=start)

    def get_user_posts(self, ):
        pass

#example
zhenya = User()
print(zhenya.user_)
posts = zhenya.get_posts(sort="active")
for post in posts:
    print(post.export())
