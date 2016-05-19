from urlparse import parse_qs


def handle(event, context):
    req_body = event['body']
    body = parse_qs(req_body)

    return {
        'response_type': 'in_channel',
        'text': body,
    }
