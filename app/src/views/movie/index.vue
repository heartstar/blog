<template>
    <transition name="fade" mode="out-in" >
        <div>
            <router-view></router-view>
        </div>          
    </transition>
</template>

<script>

export default {
    name: 'move',
    components: {  },
}
</script>

<style lang="scss" scoped>
    
</style>