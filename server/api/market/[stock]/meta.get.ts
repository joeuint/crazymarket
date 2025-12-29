export default defineEventHandler(async (event) => {
    const stock = getRouterParam(event, 'stock')?.toUpperCase();

    if (typeof stock !== 'string') {
        throw createError({
            statusCode: 400,
            statusMessage: 'Invalid stock parameter',
        });
    }

    const metadata = market.getStockMetadata(stock);

    if (metadata === null) {
        throw createError({
            statusCode: 404,
            statusMessage: 'Stock metadata not found',
        });
    }

    return metadata;
});
