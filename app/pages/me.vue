<script lang="ts" setup>
const { data: user } = await useUser();
</script>

<template>Hello {{ user?.username }}!</template>
