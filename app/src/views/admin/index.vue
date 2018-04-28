<template>
    <el-tabs v-model="activeName" type="border-card">
        <el-tab-pane label="首页配置" name="menu">
            <admin-menu></admin-menu>
        </el-tab-pane>
        <el-tab-pane label="配置管理">
            
        </el-tab-pane>
        <el-tab-pane label="角色管理">
            
        </el-tab-pane>
        <el-tab-pane label="定时任务补偿">
            
        </el-tab-pane>
    </el-tabs>
</template>

<script>

import adminMenu from '@/views/admin/menu'

export default {
    name: 'adminIndex',
    components:{
        adminMenu,
    },

    data() {
        return {
            activeName: 'menu',
        }
    }
}
</script>

<style lang="sass" scoped>

</style>

