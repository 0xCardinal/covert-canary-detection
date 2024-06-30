# Azure Login Certificate
The Azure Login Certificate Canarytoken provides you with a valid config and login certificate. Whenever an attacker tries to login using the credentails, an alert will be raised.

## Applicable Environments
Applies universally across all environments where API calls can be executed.

## How The Token Gets Triggered?
The canarytokens provides two pieces of information - 
1. Config
```json
{
  "appId": "30f85b41-be8e-4a88-89de-e7230c30291c",
  "displayName": "azure-cli-QgRTsPbcCOpRK7UYloMLW6nQDeiDc4Ea",
  "fileWithCertAndPrivateKey": "privkey",
  "password": null,
  "tenant": "c5b88def-64d6-4276-aa23-feab7321ced5"
}
```
2. PEM File (Certificate)

The token can be triggered when an attacker tried to login using the credentials - 
```bash
az login --service-principal -u 30f85b41-be8e-4a88-89de-e7230c30291c -p ~/Downloads/canary.pem --tenant c5b88def-64d6-4276-aa23-feab7321ced5
```

## How to Identify the Token Without Triggering It?
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the file is a canary token. <!-- Do not delete this line -->

The tenant and app ID remains same in the case of canary token - 
* `appId` - `30f85b41-be8e-4a88-89de-e7230c30291c`
* `tenant` - `c5b88def-64d6-4276-aa23-feab7321ced5`

Hence, this can be used to match and identify the tokens.

## Contributors
[<img src="https://github.com/0xcardinal.png" style="width:60px; height:60px;"/>](https://github.com/0xcardinal)