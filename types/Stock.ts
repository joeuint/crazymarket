export interface Stock {
  id: string;
  ticker: string;
  name: string;
  price: number;
  priceHistory: {
    date: number;
    price: number;
  }[];
}
