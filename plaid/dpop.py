from calendar import timegm
from datetime import datetime
from jose import jwt
from jose.backends import ECKey
from uuid import uuid4
from json import dumps

class OauthDPoP(object):
    def __init__(self, public_key_path, private_key_path, alg):
        self.typ    = 'dpop+jwt'
        self.alg    = alg

        self.public_key  = ECKey(open(public_key_path, 'r').read(), alg)
        self.private_key = ECKey(open(private_key_path).read(), alg)

    def generate_proof(self, claims):
        headers = {}
        headers['typ'] = self.typ
        headers['jwk'] = self.public_key.to_dict()

        claims['jti'] = str(uuid4())
        claims['ati'] = timegm(datetime.now().utctimetuple())

        return jwt.encode(claims, self.private_key, algorithm=self.alg, headers=headers)     

    def decode(self, token):
        return jwt.decode(token, key=self.public_key, algorithms=[self.alg])

    def pprint(self, token):
        print(dumps(jwt.get_unverified_header(token), sort_keys=True, indent=2))
        print(dumps(self.decode(token), sort_keys=True, indent=2))