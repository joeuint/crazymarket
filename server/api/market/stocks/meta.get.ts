export default defineEventHandler(async (event) => {
    const metas = market.getAllStockMetadata();

    return metas;
});
