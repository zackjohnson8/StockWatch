def get_all_stock_symbols_from_watchlist(json_data: dict) -> list:
    stock_list = []
    for watchlist in json_data:
        for watch_list_item in watchlist['watchlistItems']:
            stock_list.append(watch_list_item['instrument']['symbol'])
    return stock_list
