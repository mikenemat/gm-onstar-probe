# gm-onstar-probe

Remote Start Script for GM/OnStar vehicles. Needs credentials for a working OnStar account (working mobile iOS/Android app). Tested with 2014 Chevy Volt

To get it working, populate the placeholder variables at the top (device_id, username, password, pin, vin_number) 

Please share credit if used elsewhere - reverse engineering this was non-trivial. 

NOTES:

- Fixed nonces in use for the JWT/oauth handshake - no plans to fix. This 2nd layer of crypto ontop of SSL appears useless.
- The oauth handshake seems to fail periodically for no obvious reason with an "invalid_request" response - this is not handled by the script and will cause it to crash. Perhaps due to a rate-limiting function. Be smart and don't use this frivolously. Will investigate, but no promises.

Python stuff:
-Tested with latest Python 2.7.x.
-Libraries: jwcrypto, requests
