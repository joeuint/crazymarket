export default defineEventHandler(async (event) => {
    const stock = getRouterParam(event, 'stock')?.toUpperCase();
    const lastTime = Number.parseInt(getRouterParam(event, 'lastTime') || '');

    if (typeof stock !== 'string') {
        throw createError({
            statusCode: 400,
            statusMessage: 'Invalid stock parameter',
        });
    }

    const priceHistory = market.getPriceHistory(stock, lastTime);

    if (priceHistory === null) {
        throw createError({
            statusCode: 404,
            statusMessage: 'Stock prices not found',
        });
    }

    if (isNaN(lastTime)) {
        throw createError({
            statusCode: 400,
            statusMessage: 'Invalid lastTime parameter',
        });
    }

    const filteredData = priceHistory.filter((entry) => entry.timestamp >= lastTime);
    return filteredData;
});
