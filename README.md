# gm-onstar-probe

Remote Start Script for GM/OnStar vehicles. Needs credentials for a working OnStar account (working mobile iOS/Android app). Tested with 2014 Chevy Volt

To get it working, populate the placeholder variables at the top (device_id, username, password, pin, vin_number) 

Please share credit if used elsewhere - reverse engineering this was non-trivial. 

NOTES:

- I am not responsible if you get your OnStar account banned for whatever unforseen reason. 
- Nonce algorithm is loosely based on reverse engineered Android app for compatibility - no crypto lectures plz.
- The oauth handshake seems to fail periodically for no obvious reason with an "invalid_request" response - this is not handled by the script and will cause it to crash. Perhaps due to a rate-limiting function. Be smart and don't use this frivolously. Will investigate, but no promises.
- Works great with OpenHAB Exec binding - tell Alexa to remote start your car!


Python stuff:
- Tested with latest Python 2.7.x.
- Libraries: jwcrypto, requests

Usage:
- pip install jwcrypto and requests
- Edit variables on line 19-24 with your onstar creds
- Execute with Python and watch for successful output stating remote start in progress.
- If you get an error for invalid client id or bad key, check back here and get a new version. GM Probably revoked the keys from the old app. I usually catch this within a week or two and post updates. Happens once every 6-8 months.

Changelog:

June 24, 2018 - Updated with new client IDs and JWT signing key. Old ones are not working any more.

Dec 6, 2018 - Updated with new client IDs and JWT signing key. Old ones are not working any more.

Aug 5, 2019 - Updated with new client IDs and JWT signing key. Old ones are not working any more. Thanks @sradner13
