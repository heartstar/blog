<template>
    <transition name="fade" mode="out-in" >
        <div>
            <router-view></router-view>
        </div>          
    </transition>
</template>

<script>

export default {
    name: 'tools',
    components: {  },
}
</script>

<style lang="scss" scoped>
    
</style>