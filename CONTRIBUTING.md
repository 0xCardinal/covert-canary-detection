# Contribution Guidelines

## Adding Baseline Details
To contribute new information aiding in the identification of canary tokens, please add it to [indicators.md](indicators.md).

## Adding New Token's Covert Detection Techniques
1. Create a new file within the [tokens/](tokens/) directory.
2. Name the file to match the token's name as listed on canarytokens.org.
3. Use the following template to add information for each tokens:

```markdown
# Token Name 
Brief description of the token's purpose and use case.

## Applicable Environments
Include details about operating systems like Windows, MacOS, or any other relevant environment specifics that can help prevent triggering the tokens.

## How The Token Gets Triggered?
Describe the conditions or actions that cause the token to trigger. Include technical specifics if known, such as protocols used, required inputs, or environmental triggers.

## How to Identify the Token Without Triggering It?
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the file is a canary token. <!-- Do not delete this line -->

Explain methods or indicators to recognize the presence of the token without causing it to trigger. This may involve examining metadata, file attributes, network behavior, or other observable characteristics.

## References/Comments/Remarks
Include any additional comments, remarks, or references related to the token, such as known vulnerabilities, related research, or historical context.

## Contributors
Provide information about the contributor(s) who documented or discovered this token. Include their name, affiliation, and contact information if applicable. Use the following code to add your profile - 
[<img src="https://github.com/{{contributor}}.png" style="width:60px; height:60px;"/>](https://github.com/{{contributor}})
```

## Contact
For any queries or concern, feel free to contact.
