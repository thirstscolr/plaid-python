import argparse
import time
import plaid
from plaid.api import plaid_api
from plaid.model.country_code import CountryCode
from plaid.model.products import Products

from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.item_get_request import ItemGetRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser

# mavery
# CLIENT_ID="66466b2502e096ca6c2e54cf"
# SECRET="daad84662060520554b3347814827e"
# ACCESS_TOKEN="access-devenv-6dda8e22-779a-43b3-81ec-40466c1e83e3"

# Ani
# host="http://aveeraragavan.devenv.plaid.io:50022",
# api_key={
#     "clientId": "6644d4313b8fe7be6c66e132",
#     "secret": "b66ab31f201f96e6082b2f8975a32a",
#     "oauthDpop": "true",
# },
# access_token = "access-devenv-92742fa8-20bb-4cf1-99c5-b22226c48036"

# Demo 1: Happy path
# python dpop_demo.py --client_id '6644d4313b8fe7be6c66e132' --endpoint '/item/get' --access_token 'access-devenv-92742fa8-20bb-4cf1-99c5-b22226c48036'
# Demo 2: Client ID doesn't match
# python dpop_demo.py --client_id '6644d4313b8fe7be6c66e132' --endpoint '/item/get' --access_token 'access-devenv-92742fa8-20bb-4cf1-99c5-b22226c48036' --spoof_claim 'client_id' --value '40e7ba71d728eaf801c0ea9a'
# Demo 3: Replay attack (expiration)
## python dpop_demo.py --client_id '6644d4313b8fe7be6c66e132' --endpoint '/item/get' --access_token 'access-devenv-92742fa8-20bb-4cf1-99c5-b22226c48036' --spoof_claim 'iat' --value 10 ;#(10 mins ago)

CLIENT_NAME = "Oauth DPoP Test 2"

def main():
  try:
    parser = argparse.ArgumentParser(
        description="Send a request to the Plaid API using DPoP"
    )

    parser.add_argument("--client_id", default='66466b2502e096ca6c2e54cf', action='store')
    parser.add_argument("--endpoint", choices=["/item/get", "/auth/get", "/link/token/create"])
    parser.add_argument("--access_token", default='access-devenv-6dda8e22-779a-43b3-81ec-40466c1e83e3', action='store')
    parser.add_argument("--spoof_claim", action='store', choices=['client_id', 'access_token', 'iat', 'htu', 'htm'])
    parser.add_argument("--value", action='store')
    args = parser.parse_args()

    configuration = plaid.Configuration(
 #       host="http://mavery.devenv.plaid.io:50022",
        host="http://aveeraragavan.devenv.plaid.io:50022",
 
        api_key={
            "clientId": args.client_id,
#            "secret": "daad84662060520554b3347814827e",
            "secret": 'b66ab31f201f96e6082b2f8975a32a', #ani
            "oauthDpop": "true",
        },
        public_key_path="./tests/keys/public.pem",
        private_key_path="./tests/keys/private.ec.key",
        alg="ES256",
        claim_to_spoof={}
    )

    if args.spoof_claim:
        configuration.claim_to_spoof = {args.spoof_claim: args.value}

    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    if args.endpoint == "/item/get":
        item_request = ItemGetRequest(access_token=args.access_token)
        response = client.item_get(item_request)
        print("item_id: ", response["item"]["item_id"])
    elif args.endpoint == "/auth/get":
        ag_request = AuthGetRequest(access_token=args.access_token)
        response = client.auth_get(ag_request)
        print("item_id: %s", response["item"]["item_id"])
    elif args.endpoint == "/link/token/create":
        request = LinkTokenCreateRequest(
            products=[Products("auth"), Products("transactions")],
            client_name=CLIENT_NAME,
            country_codes=[CountryCode("US")],
            language="en",
            user=LinkTokenCreateRequestUser(client_user_id=str(time.time())),
        )
        response = client.link_token_create(request)
        print(response["link_token"])
  except Exception as e:
     print(e)


if __name__ == "__main__":
    main()
