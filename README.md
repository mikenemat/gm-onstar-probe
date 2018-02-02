# gm-onstar-probe

I drive a Chevy Volt. Great car. GM's restrictions and obfuscations around IP connectivity....not so great.

Here's a script to get you partly there. One day this will be fully functional for beginners to use. Right now, it still involves quite a bit of work. To get it working, populate the placeholder variables at the top. This requires significant reverse-engineering of your own android app traffic...for now.

Use this script with whatever HA platform you want to get cool features like "Alexa! Remote start my Volt". 

Please share credit if used elsewhere - reverse engineering this was non-trivial. 

NOTES:

- Fixed nonces in use for the JWT/oauth handshake...will be fixed soon
- Client Ids and Device Ids need to be reverse engineered from your own Android app...workaround for this coming soon.
^ Disabling cert pinning to figure this out is fun.
