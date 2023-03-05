# Monitoring Webpage changes

This is a simple tool that monitors changes in any webpage that can be crawled.
It's quite simple how it works. I used beautifulsoup4 for the web scrapping. requests, well for the requests :smile: 
when the html comes in its body is checked against the caches to see what has changed. If the local files don't 
exist they are created and monitoring starts. Most of the features lack the thorough testing they deserve, but they'll get it.

## Features.
- ~~Url validation.~~ At the moment the tool will only support http protocol
- ~~changes highlighting.~~ The changes that have been made to the site are displayed on the console. maybe a gui would be better? 
- ~~Monitoring Frequency:~~ How often monitoring should happen. it is better to have low frequency otherwise your ip maybe blocked if too many requests are coming from it. this can be solved by using proxies.
- Alerts. I'm thinking  Email but ill explore other options.
- Full Website monitoring. will definitely add this. might require a spider though
- Html and styling related to what has changed: It is better to alert with the exact changes that have happened to the site even design changes
- 

I need to ask a few questions?