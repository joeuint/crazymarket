<script setup lang="ts">
import type { Stock } from '@@/types/Stock';

const props = defineProps<{ stock: Stock }>();

const curveType = CurveType.Linear;

const categories = {
    price: {
        name: 'Price',
        color: '#3b82f6',
    },
};
</script>

<template>
    <div class="bg-neutral-950 p-6 px-24 rounded-lg shadow-md w-3xl">
        <!-- Stock Info -->
        <div class="flex items-center justify-between">
            <div class="">
                <h2 class="text-3xl font-semibold">{{ $props.stock.name }}</h2>
                <span class="text-neutral-400 font-semibold">{{ $props.stock.ticker }}</span>
            </div>
            <div>
                <span class="text-2xl font-bold">${{ $props.stock.price.toFixed(2) }}</span>
            </div>
        </div>
        <LineChart
            class="px-6 mt-20"
            :data="$props.stock.priceHistory"
            :categories="categories"
            :height="300"
            xLabel="Date"
            yLabel="Amount"
            :curveType="curveType"
        />
    </div>
</template>
