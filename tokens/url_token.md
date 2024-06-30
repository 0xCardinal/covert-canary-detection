# URL/Web Token
A URL/Web token from canarytokens.org is a special type of token that triggers an alert when a specific URL is accessed. This is typically used to detect unauthorized access or exfiltration attempts.

## Applicable Environments
This token is applicable in any environment where URLs can be accessed through a web browser or other web-based application.

## How The Token Gets Triggered
The token gets triggered when the specific URL associated with the token is accessed. The URL will resolve the specified domain, which then sends a callback to the defined URL, indicating that the token has been triggered.

## How to Identify the Token Without Triggering It
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the token is a canary token. <!-- Do not delete this line -->

To identify if a URL/Web token is a canary token, follow these steps:
1. Observe the URL - `http://canarytokens.com/tags/static/ry5osq5ds345c4d0mddqe02uo/post.jsp`, it contains one of the domains mentioned in the [`indicators.md`](../indicators.md) file, which confirms that the URL is a canary token.

## References/Comments/Remarks
The way it is different from [DNS Token Canary Token](./dns_token.md), it needs the URL to resolve in order to send the alert.

## Contributors
[<img src="https://github.com/0xcardinal.png" style="width:60px; height:60px;"/>](https://github.com/0xcardinal)