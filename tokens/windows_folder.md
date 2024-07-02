# Windows Folder Token
A Windows Folder token triggers an alert when a specific folder on a Windows system is accessed. This is typically used to detect unauthorized access to sensitive directories.

## Applicable Environments
This token is applicable in any Windows environment where folders can be accessed or monitored.

## How The Token Gets Triggered
The token gets triggered when the specific folder associated with the token is accessed. The access event sends a callback to the defined URL, indicating that the token has been triggered.

The folder has a `desktop.ini` file that contains the following data - 
```powershell
[.ShellClassInfo]
IconResource=\\%USERNAME%.%COMPUTERNAME%.%USERDOMAIN%.INI.8zjnkwpxs6fcmgv1fj3lfe1sd.canarytokens.com\resource.dll
```

- `[.ShellClassInfo]`: This section specifies that the following lines contain information about the folder's appearance.
- `IconResource`: Specifies the path to an icon resource. Windows will attempt to load this icon when the folder is accessed.

and the token has `system` & `read-only` folder permission - `attrib +s +r "C:\Path\To\Your\Folder"`. It resembles a folder but is not actually one.

## How to Identify the Token Without Triggering It
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the token is a canary token. <!-- Do not delete this line -->

To identify if a Windows folder is a canary token, follow these steps:
1. Open the folder, using the terminal won't trigger the alert.
2. The trigger only works when the folder is opened using the GUI and using click method.
3. Open the terminal and inspect the folder for `desktop.ini` file with the above mentioned code. 

## Contributors
[<img src="https://github.com/0xcardinal.png" style="width:60px; height:60px;"/>](https://github.com/0xcardinal)
[<img src="https://github.com/acc3ssp0int-official.png" style="width:60px; height:60px;"/>](https://github.com/acc3ssp0int-official)
