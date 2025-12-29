<script setup lang="ts">
import Stock from '@/components/Stock.vue';
import type { Stock as StockType } from '@@/types/Stock';

const stocks = reactive<StockType>({
    id: '668a82a3-6b93-4441-a799-365fa4dc4854',
    ticker: 'CRBK',
    name: 'Crazy Bank',
    price: 67,
    priceHistory: [
        { date: 0, price: 50 },
        { date: 10, price: 55 },
        { date: 20, price: 53 },
        { date: 30, price: 60 },
        { date: 40, price: 62 },
        { date: 50, price: 65 },
        { date: 60, price: 70 },
        { date: 70, price: 68 },
        { date: 80, price: 72 },
        { date: 90, price: 71 },
        { date: 100, price: 58 },
        { date: 110, price: 50 },
        { date: 120, price: 45 },
        { date: 130, price: 44 },
        { date: 140, price: 47 },
        { date: 150, price: 56 },
        { date: 160, price: 49 },
        { date: 170, price: 57 },
        { date: 180, price: 53 },
        { date: 190, price: 50 },
        { date: 200, price: 54 },
        { date: 210, price: 50 },
        { date: 220, price: 62 },
        { date: 230, price: 63 },
        { date: 240, price: 64 },
        { date: 250, price: 64 },
        { date: 260, price: 66 },
        { date: 270, price: 68 },
        { date: 280, price: 64 },
        { date: 290, price: 56 },
        { date: 300, price: 58 },
        { date: 310, price: 67 },
    ],
});
</script>

<template>
    <div class="text-primary flex items-center gap-2 mb-6">
        <Icon name="i-fluent:chart-multiple-20-filled" size="45" />
        <h1 class="font-semibold text-3xl my-8">Market</h1>
    </div>
    <Stock :stock="stocks" />
</template>
