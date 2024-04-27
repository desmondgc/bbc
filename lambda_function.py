import os
import re
import urllib.request

# E.g. <guid isPermaLink="false">https://www.bbc.co.uk/news/world-asia-china-68905475#0</guid>
frag_guid = re.compile(r"#\d+</guid>")

def lambda_handler(event, context):
    """Remove URL fragments from guids in an RSS feed."""
    with urllib.request.urlopen(os.environ["FEED_URL"]) as feed:
        rss = frag_guid.sub(r"</guid>", feed.read().decode())

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/xml"
        },
        "body": rss
    }
