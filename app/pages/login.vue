<script setup lang="ts">
const toast = useToast();

const { data: userContext } = await useUser();

const providers = [
    {
        label: 'GitHub',
        icon: 'i-simple-icons-github',
        onClick: () => {
            window.location.href = '/api/auth/github';
        },
    },
];
</script>

<template>
    <div class="min-h-screen flex justify-center items-center" v-if="!userContext">
        <UPageCard class="w-full max-w-md">
            <UAuthForm
                title="Welcome back to CrazyMarket"
                description="Log in to manage your portfolio and trade stocks in the craziest market ever."
                :providers="providers"
            />
        </UPageCard>
    </div>
    <div v-else>
        <p>
            You are already logged in as {{ userContext.user.username }}. Go to the
            <NuxtLink to="/market" class="reglink">market</NuxtLink>
            to start trading!
        </p>
    </div>
</template>
