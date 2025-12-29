<script lang="ts" setup>
const links = ref([
    {
        label: 'See the market',
        to: '/market',
        icon: 'i-fluent-chart-multiple-20-filled',
    },
    {
        label: 'Sign Up',
        to: '/login',
        color: 'neutral' as const,
        variant: 'subtle' as const,
        icon: 'i-fluent-person-add-20-filled',
    },
]);
</script>

<template>
    <UPageHero
        title="CrazyMarket"
        description="Trade stocks in a fantasy world with crazy events and unpredictable market
    movements. Can you survive the tides of the craziest stock market ever?"
        headline="New!"
        :links="links"
    >
    </UPageHero>
</template>
