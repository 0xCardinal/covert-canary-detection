# Unique Email Address
An email address token is a type of token that triggers an alert when a specific email address is used. This is typically used to detect unauthorized use or distribution of the email address.

## Applicable Environments
This token is applicable in any environment where email addresses can be sent or received, such as email clients, servers, or web forms.

## How The Token Gets Triggered?
The token gets triggered when an email is sent to the specific email address associated with the token. The email server logs the event and sends a callback to the defined URL, indicating that the token has been triggered.

## How to Identify the Token Without Triggering It?
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the token is a canary token. <!-- Do not delete this line -->

To identify if an email address is a canary token, follow these steps:
1. Observe the domain, the email is created off - `2ya72bit4osf8ruw69fn43lwv@canarytokens.com`
2. Match it with the list of domains from the [`indicators.md`](../indicators.md)

## Contributors
[<img src="https://github.com/0xcardinal.png" style="width:60px; height:60px;"/>](https://github.com/0xcardinal)