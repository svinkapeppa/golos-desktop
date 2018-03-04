from piston import Steem
from piston import account


class User:

    def __init__(self, login="golosproject", password="qwerty12345"):
        self.steem_instance_ = Steem(node="wss://ws.testnet3.golos.io", rpcuser=login, rpcpassword=password)
        self.user_ = account.Account(account_name=login, steem_instance=self.steem_instance_)
        print(self.user_.get('name'))

    def get_posts(self, limit=10,
                  sort="active",
                  category=None,
                  start=None):
        # list of dicts
        return self.steem_instance_.get_posts(limit=limit, sort=sort, category=category, start=start)

    # cause of Golos API doesnt work
    def get_user_posts(self):
        return self.steem_instance_.get_blog(self.user_.get('name'))

    def post(self,
             title,
             body,
             category=None,
             tags=[]):

        self.steem_instance_.post(title, body,
                                  author=self.user_.get('name'),
                                  category=category,
                                  tags=tags)
# example 1
zhenya = User()
print(zhenya.user_)

# example 2
posts = zhenya.get_posts(sort="active")
for post in posts:
    print(post['id'])
    print(post.export())

# example 3
"""
posts = zhenya.get_user_posts()
for post in posts:
    print(post.export())
"""

# example 4
zhenya.post(title="Bang bang bang", body="<p> HELLO! </p>")
