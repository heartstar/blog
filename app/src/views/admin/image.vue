<template>
    <div class="article">
        <div class="btns">
            <el-input v-model="imageId" size="mini"></el-input>
            <el-button type="primary" size="mini" class="add" @click="addData()">新增</el-button>
        </div>   
        <div>
            <div class="img" v-for="(item, index) in 10" :key="index">
                <img src="http://element.eleme.io/static/hamburger.50e4091.png" alt="">
                <span>{{ index }}</span>
            </div>
        </div> 
    </div>
</template>

<script>
import { getImage } from '@/api/getData'

export default {
    name: 'adminImage',

    data() {
        return {
            tableData: null,
            imageId: null,
        }
    },

    created() {
        this.init();
    },

    methods: {

       
        addData(){   
            getImage(this.imageId).then(res =>{
                console.log(res)
            }).catch(err =>{})
        },

        
    }
}
</script>

<style lang="scss" scoped>
    .img{
        float: left;
    }
</style>

