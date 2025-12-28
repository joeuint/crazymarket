<script setup lang="ts">
import type { Stock } from "@@/types/Stock";

const props = defineProps<{ stock: Stock }>();

const curveType = CurveType.Linear;

const data = [
  { date: 0, price: 100 },
  { date: 5, price: 105 },
  { date: 10, price: 102 },
  { date: 15, price: 108 },
  { date: 20, price: 112 },
  { date: 25, price: 110 },
  { date: 30, price: 115 },
  { date: 35, price: 120 },
  { date: 40, price: 118 },
  { date: 45, price: 122 },
  { date: 50, price: 125 },
  { date: 55, price: 75 },
  { date: 60, price: 20 },
  { date: 65, price: 0 },
  { date: 70, price: 15 },
  { date: 75, price: 50 },
  { date: 80, price: 85 },
  { date: 85, price: 110 },
  { date: 90, price: 130 },
  { date: 95, price: 148 },
  { date: 100, price: 160 },
  { date: 105, price: 155 },
  { date: 110, price: 158 },
  { date: 115, price: 162 },
  { date: 120, price: 170 },
  { date: 125, price: 180 },
  { date: 130, price: 190 },
  { date: 135, price: 200 },
  { date: 140, price: 195 },
  { date: 145, price: 198 },
  { date: 150, price: 100 },
  { date: 155, price: 105 },
  { date: 160, price: 110 },
  { date: 165, price: 115 },
  { date: 170, price: 120 },
  { date: 175, price: 125 },
  { date: 180, price: 130 },
  { date: 185, price: 135 },
  { date: 190, price: 140 },
  { date: 195, price: 145 },
  { date: 200, price: 2 },
];

const categories = {
  price: {
    name: "Price",
    color: "#3b82f6",
  },
};
</script>

<template>
  <div class="bg-neutral-950 p-6 px-24 rounded-lg shadow-md w-3xl">
    <!-- Stock Info -->
    <div class="flex items-center justify-between">
      <div class="">
        <h2 class="text-3xl font-semibold">{{ $props.stock.name }}</h2>
        <span class="text-neutral-400 font-semibold">{{
          $props.stock.ticker
        }}</span>
      </div>
      <div>
        <span class="text-2xl font-bold"
          >${{ $props.stock.price.toFixed(2) }}</span
        >
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
