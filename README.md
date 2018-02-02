# gm-onstar-probe

I drive a Chevy Volt. Great car. GM's restrictions and obfuscations around IP connectivity....not so great.

This script is really rough with debug code everywhere, but it works. Populate the placeholder variables at the top. 

Use this script with whatever HA platform you want to get cool features like "Alexa! Remote start my Volt". 

Please share credit if used elsewhere - reverse engineering this was non-trivial. 

NOTES:

- Fixed nonces in use for the JWT/oauth handshake...will be fixed soon
- Client Ids and Device Ids need to be reverse engineered from your own Android app...workaround for this coming soon.
^ Disabling cert pinning to figure this out is fun.
