<script setup lang="ts">
import Stock from '@/components/Stock.vue';

const stocks = await $fetch('/api/market/stocks/meta');
</script>

<template>
    <div class="text-primary flex items-center gap-2 mb-6">
        <Icon name="i-fluent:chart-multiple-20-filled" size="45" />
        <h1 class="font-semibold text-3xl my-8">Market</h1>
    </div>
    <div class="mb-4 grid-cols-2 grid gap-4">
        <Stock :stock="stock" v-for="stock in stocks" :key="stock.stock_ticker" />
    </div>
</template>
