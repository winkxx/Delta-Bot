def get_uploader_url(uploader="Prof"):
    return f"https://1337x.uproxy.workers.dev/{uploader}-torrents"


def get_query_url(query="QxR", order_by="seeds"):
    if order_by == "seeds":
        return f"https://1337x.uproxy.workers.dev/sort-search/{query}/seeders/desc"
    elif order_by == "time":
        return f"https://1337x.uproxy.workers.dev/sort-search/{query}/time/desc"
