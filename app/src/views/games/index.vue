<template>
    <transition name="fade" mode="out-in" >
        <div>
            <router-view></router-view>
        </div>          
    </transition>
</template>

<script>

export default {
    name: 'games',
    components: {  },
}
</script>

<style lang="scss" scoped>
    
</style>