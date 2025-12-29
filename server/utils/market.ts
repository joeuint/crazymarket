import Database from 'better-sqlite3';

const db = new Database('market.db');

export interface MarketDataEntry {
    stock_name: string;
    price_cents: number;
    timestamp: number;
}

export const market = {
    isMarketDataEntry(obj: any): obj is MarketDataEntry {
        return (
            obj &&
            typeof obj.stock_name === 'string' &&
            typeof obj.price_cents === 'number' &&
            typeof obj.timestamp === 'number'
        );
    },

    getCurrentPrice(name: string): MarketDataEntry | null {
        const row =
        db.prepare('SELECT stock_name, price_cents, timestamp FROM market_data WHERE stock_name = ? ORDER BY timestamp DESC LIMIT 1')
            .get(name);

        if (row && this.isMarketDataEntry(row)) {
            return row;
        }

        return null;
    }
};