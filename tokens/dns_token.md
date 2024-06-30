# DNS Token
A DNS token from canarytokens.org is a special type of token that triggers an alert when a specific DNS query is made. This is typically used to detect unauthorized access or exfiltration attempts.

## Applicable Environments
This token is applicable in any environment where DNS queries can be made.

## How The Token Gets Triggered?
The token gets triggered when a DNS query for the specific domain associated with the token is made. The DNS query will resolve the specific URL, which then sends a callback to the defined URL, indicating that the token has been triggered.

## How to Identify the Token Without Triggering It?
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the token is a canary token. <!-- Do not delete this line -->

To identify if a DNS token is a canary token, follow these steps:
1. Observe the URL - `ecnvji3orhp8h86ga7wx63fxm.canarytokens.com`, it contains one of the domains mentioned in the [`indicators.md`](../indicators.md) file, which confirms that the URL is a canary token.

## References/Comments/Remarks
The way it is different from [URL/Web Token Canary Token](./url_token.md), DNS token will send the alert, even when the URL is hit or a DNS query is made.
   
## Contributors
[<img src="https://github.com/0xcardinal.png" style="width:60px; height:60px;"/>](https://github.com/0xcardinal)
