export interface MarketDataEntry {
    stock_ticker: string;
    price_cents: number;
    timestamp: number;
}

export interface StockMetadata {
    stock_ticker: string;
    stock_name: string;
    biography: string;
}
