<script lang="ts" setup>
const { data: userContext } = await useUser();
</script>

<template>
    <nav class="p-4 flex justify-between items-center border-b-2 border-b-gray-700">
        <!-- Left -->
        <div class="">
            <NuxtLink to="/" class="">
                <span class="text-2xl font-semibold"> <span class="text-primary">Crazy</span>Market </span>
            </NuxtLink>
        </div>

        <!-- Center -->
        <div>
            <ul class="flex gap-6 font-semibold">
                <li>
                    <NuxtLink to="/market" class="hover:text-primary flex items-center gap-1">
                        <Icon size="25" name="i-fluent-chart-multiple-20-filled"></Icon>
                        <span>Market</span>
                    </NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/portfolio" class="hover:text-primary flex items-center gap-1">
                        <Icon size="25" name="i-fluent-money-20-filled"></Icon>
                        <span>Portfolio</span>
                    </NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/leaderboard" class="hover:text-primary flex items-center gap-1">
                        <Icon size="25" name="i-fluent-trophy-20-filled"></Icon>
                        <span>Leaderboard</span>
                    </NuxtLink>
                </li>
            </ul>
        </div>

        <!-- Right -->
        <div>
            <div class="flex items-center gap-4">
                <span class="text font-semibold">
                    Hello, {{ userContext?.user.username ?? 'Guest' }}!
                    <span v-if="!userContext" class="inline-block">
                        <NuxtLink class="reglink" to="/login">Login?</NuxtLink>
                    </span>
                </span>
                <NuxtLink :to="userContext ? '/profile' : '/login'">
                    <UAvatar
                        icon="i-fluent-person-20-filled"
                        :src="userContext?.profile?.avatarUrl ?? undefined"
                        :alt="userContext?.user.username"
                        size="lg"
                    >
                    </UAvatar>
                </NuxtLink>
            </div>
        </div>
    </nav>
</template>
