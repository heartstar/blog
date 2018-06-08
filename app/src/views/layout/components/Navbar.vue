<template>
    <div class="menu" ref="elMenu">
        <div class="demo">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="navbar">
                            <el-button type="primary" size="mini">Menu</el-button>
                            <ul class="menu">
                                <li><router-link :to="{path: '/'}" class="fa fa-home" title="首页"></router-link></li>
                                <li><router-link :to="{path: '/article'}" class="fa fa-book" title="随手小记"></router-link></li>
                                <li><router-link :to="{path: '/tools'}" class="fa fa-wrench" title="小工具"></router-link></li>
                                <li><router-link :to="{path: '/movie'}" class="fa fa-video-camera" title="休闲一刻"></router-link></li>
                                <li><router-link :to="{path: '/games'}" class="fa fa-gamepad" title="小游戏"></router-link></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {  } from '@/api/getData'
export default {
    data() {
        return {
            
        };
    },

    created() {

    },

    methods: {

    }
}
</script>
<style lang="scss" scoped>
.menu{
    position: fixed;
    bottom: 200px;
    left: 40px;
    width: 0px;
    height: 0px;
    z-index: 99;
    border-radius: 50%;
    transform: scale(0.9);
    transition: all .3s ease;
    .el-button{
        padding: 0;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        text-align: center;
    }
}
.navbar{
    line-height: 150px;
    text-align: center;
    font-size: 1.75em;
    font-weight: bold;
}
.navbar:hover{
    background: rgba(255, 255, 255, 0.75);
}
.navbar .menu{
    list-style: none;
    padding: 0;
    margin: 0;
    position: absolute;
    top: -27px;
    left: -78px;
    border: 130px solid transparent;
    cursor: default;
    border-radius: 50%;
    transform: scale(0);
    transition: transform 1.4s 0.07s;
    z-index: -1;
}
.navbar:hover .menu{
    transition: transform 0.4s 0.08s, z-index   0s  0.5s;
    transform: scale(1);
    z-index: 1;
}
.navbar .menu li{
    position: absolute;
    top: -100px;
    left: -100px;
    transform-origin: 80px 80px;
    transition: all 0.5s 0.1s;
}
.navbar:hover .menu li{
    transition: all 0.6s;
}
.navbar .menu li a{
    width: 45px;
    height: 45px;
    line-height: 45px;
    border-radius: 50%;
    background: #cfcfcf;
    position: absolute;
    font-size: 60%;
    color: #99b977;
    transition: 0.6s;
}
.navbar:hover .menu li:nth-child(1){
    transition-delay: 0.02s;
    transform: rotate(85deg);
}
.navbar:hover .menu li:nth-child(1) a{
    transition-delay: 0.04s;
    transform: rotate(635deg);
}
.navbar:hover .menu li:nth-child(2){
    transition-delay: 0.04s;
    transform: rotate(125deg);
}
.navbar:hover .menu li:nth-child(2) a{
    transition-delay: 0.08s;
    transform: rotate(595deg);
}
.navbar:hover .menu li:nth-child(3){
    transition-delay: 0.06s;
    transform: rotate(165deg);
}
.navbar:hover .menu li:nth-child(3) a{
    transition-delay: 0.12s;
    transform: rotate(555deg);
}
.navbar:hover .menu li:nth-child(4){
    transition-delay: 0.08s;
    transform: rotate(205deg);
}
.navbar:hover .menu li:nth-child(4) a{
    transition-delay: 0.16s;
    transform: rotate(515deg);
}
.navbar:hover .menu li:nth-child(5){
    transition-delay: 0.1s;
    transform: rotate(245deg);
}
.navbar:hover .menu li:nth-child(5) a{
    transition-delay: 0.2s;
    transform: rotate(475deg);
}
</style>