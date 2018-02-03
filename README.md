# gm-onstar-probe

I drive a Chevy Volt. Great car. GM's restrictions and obfuscations around IP connectivity....not so great.

To get it working, populate the placeholder variables at the top.

Use this script with whatever HA platform you want to get cool features like "Alexa! Remote start my Volt". 

Please share credit if used elsewhere - reverse engineering this was non-trivial. 

NOTES:

- Fixed nonces in use for the JWT/oauth handshake - no plans to fix. This 2nd layer of crypto ontop of SSL appears useless.
- The oauth handshake seems to fail periodically for no obvious reason with an "invalid_request" response - this is not handled by the script and will cause it to crash. Perhaps due to a rate-limiting function. Be smart and don't use this frivolously.
