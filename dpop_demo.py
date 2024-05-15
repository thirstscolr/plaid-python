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

CLIENT_NAME = "Oauth DPoP Test"

configuration = plaid.Configuration(
    host="http://mavery.devenv.plaid.io:50022",
    api_key={
        "clientId": "6643d8f302e096ece206d86d",
        "secret": "62a1ce21125fc66b1cf894ee269e2a",
        "oauthDpop": "true",
    },
    public_key_path="./tests/keys/public.pem",
    private_key_path="./tests/keys/private.ec.key",
    alg="ES256",
    claim_to_spoof={'clientId': 'foobar'}
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

access_token = "access-devenv-35e4c555-17c9-4bcd-a62c-63072d750cea"


def main():
  try:
    parser = argparse.ArgumentParser(
        description="Send a request to the Plaid API using DPoP"
    )
    parser.add_argument("endpoint", choices=["item", "auth", "ltc"])
    args = parser.parse_args()

    if args.endpoint == "item":
        item_request = ItemGetRequest(access_token=access_token)
        response = client.item_get(item_request)
        print(response["item"]["item_id"])
    elif args.endpoint == "auth":
        ag_request = AuthGetRequest(access_token=access_token)
        response = client.auth_get(ag_request)
        print(response["item"]["item_id"])
    elif args.endpoint == "ltc":
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
