<template>
    <div class="dashboard-container">
        <div class="carousel">
            <el-carousel :interval="4000" type="card" height="300px">
                <el-carousel-item v-for="item in 6" :key="item">
                <h3>{{ item }}</h3>
                </el-carousel-item>
            </el-carousel>
        </div>      
    </div>
</template>

<script>

export default {
    name: 'dashboard',
    components: {  },
}
</script>

<style lang="scss" scoped>
.carousel{
    width: 60%;
    margin: 0 auto;
    height: 50vh;
    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        margin: 0;
    }
    
    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }
    
    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
}
</style>