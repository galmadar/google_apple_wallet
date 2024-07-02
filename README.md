# google_apple_wallet

## Google Demo
[google-wallet-demo](google-wallet-demo)

you have there 2 directories in order to communicate with the Google Wallet API

#### in [the python directory](google-wallet-demo/python) you have [main.py](google-wallet-demo/python/main.py) that you can run

* pay attention to configure the path to the service account `json` file in each `demo_...` file you use
* pay attention to set the `issuer_id` in the `main.py` file


## Apple Demo

[apple-wallet-demo](apple-wallet-demo)

Read the [README.md](apple-wallet-demo/README.md) of apple in order to generate pkpass file

#### [SamplePasses](apple-wallet-demo/SamplePasses)
in this directory we have some samples of some kinds of passes generated for apple.

** pay attention to update in each `pass.json` the  `passTypeIdentifier` and `teamIdentifier` fields to your Pass Type Id and Team Id