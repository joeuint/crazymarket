import Database from 'better-sqlite3';

const db = new Database('market.db');

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

export const market = {
    isMarketDataEntry(obj: any): obj is MarketDataEntry {
        return (
            obj &&
            typeof obj.stock_ticker === 'string' &&
            typeof obj.price_cents === 'number' &&
            typeof obj.timestamp === 'number'
        );
    },

    isStockMetadata(obj: any): obj is StockMetadata {
        return (
            obj &&
            typeof obj.stock_ticker === 'string' &&
            typeof obj.stock_name === 'string' &&
            typeof obj.biography === 'string'
        );
    },

    getCurrentPrice(ticker: string): MarketDataEntry | null {
        const row = db
            .prepare(
                'SELECT stock_ticker, price_cents, timestamp FROM market_data WHERE stock_ticker = ? ORDER BY timestamp DESC LIMIT 1',
            )
            .get(ticker);

        if (row && this.isMarketDataEntry(row)) {
            return row;
        }

        return null;
    },

    getStockMetadata(ticker: string): StockMetadata | null {
        const row = db
            .prepare('SELECT stock_ticker, stock_name, biography FROM stocks_meta WHERE stock_ticker = ?')
            .get(ticker);

        if (row && this.isStockMetadata(row)) {
            return row;
        }

        return null;
    },
};
