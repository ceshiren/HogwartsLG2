from mitmproxy import http

def request(flow: http.HTTPFlow):
    # redirect to different host
    if "quote.json" in flow.request.url:
        with open("/Users/lixu/project/tmp/quote.json") as f:
            flow.response = http.HTTPResponse.make(
                200, f.read(),
            )


