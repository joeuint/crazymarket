<script setup lang="ts">
import Navbar from './components/Navbar.vue';
</script>

<template>
    <div>
        <NuxtRouteAnnouncer />
        <UApp>
            <UMain>
                <Navbar />
                <NuxtLayout>
                    <UContainer>
                        <NuxtPage />
                    </UContainer>
                </NuxtLayout>
            </UMain>
        </UApp>
    </div>
</template>

<style></style>
