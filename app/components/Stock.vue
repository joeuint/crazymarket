<script setup lang="ts">
import type { StockMetadata } from '@@/types/Stock';

const props = defineProps<{ stock: StockMetadata }>();

const curveType = CurveType.Linear;

const categories = {
    price: {
        name: 'Price',
        color: '#3b82f6',
    },
};

const price = reactive(await $fetch(`/api/market/${props.stock.stock_ticker}/priceHistory`, {}));

const priceData = computed(() => {
    return price
        .map((entry: { price_cents: number; timestamp: number }) => ({
            date: entry.timestamp * 1000, // Convert seconds to milliseconds for Date constructor
            price: entry.price_cents / 100,
        }))
        .reverse();
});
</script>

<template>
    <div class="bg-neutral-950 p-6 px-12 rounded-lg shadow-md w-full">
        <!-- Stock Info -->
        <div class="flex items-center justify-between">
            <div class="">
                <h2 class="text-3xl font-semibold">{{ $props.stock.stock_name }}</h2>
                <span class="text-neutral-400 font-semibold">{{ $props.stock.stock_ticker }}</span>
            </div>
            <div>
                <span class="text-2xl font-bold" v-if="price[0]">${{ price[0].price_cents / 100 }}</span>
            </div>
        </div>
        <LineChart
            class="px-6 mt-20"
            :data="priceData"
            :categories="categories"
            :height="300"
            xLabel="Date"
            yLabel="Amount"
            :curveType="curveType"
            :xFormatter="
                (i: number) =>
                    priceData[i]
                        ? new Date(priceData[i].date).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' })
                        : ''
            "
        />
    </div>
</template>
