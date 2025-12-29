export default defineEventHandler(async (event) => {
    const stock = getRouterParam(event, 'stock')?.toUpperCase();
    console.log(stock);

    if (typeof stock !== 'string') {
        throw createError({
            statusCode: 400,
            statusMessage: 'Invalid stock parameter',
        });
    }

    const dataEntry = market.getCurrentPrice(stock);

    if (dataEntry === null) {
        throw createError({
            statusCode: 404,
            statusMessage: 'Stock not found',
        });
    }

    return dataEntry;
});
