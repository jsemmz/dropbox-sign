from hellosign_sdk import HSClient
from decouple import config 

dropbox_api_key = config('DROPBOX_API_KEY')

client = HSClient(api_key=dropbox_api_key)

client.get_account_info()
print(client.account.email_address)

files = ['example.pdf']

signers = [
    {'name': 'Dropbox Dev', 'email_address': 'stashdev@outlook.com'},
]

cc_email_addresses = ['hello@example.com']

signature_request = client.send_signature_request(
    test_mode=True,
    files=files,
    file_urls=None,
    title='Example from Dropbox Dev',
    subject='The document we discussed',
    message='Sign this document please',
    signing_redirect_url=None,
    signers=signers,
    cc_email_addresses=cc_email_addresses
)

print(signature_request.signature_request_id)