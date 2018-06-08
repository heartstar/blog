<template>
    <div>
        <section class="tools">
            <ul class="nav">
                <li v-for="(item, index) in tools" :key="index">
                    <a :href="item.href" target="_blank">{{ item.title }}</a>
                </li>
            </ul>
        </section>
    </div>
</template>

<script>
import { getTools } from '@/api/getData'
export default {
    name: 'toolset',
    components:{

    },
    data() {
        return {
            tools: null,
        };
    },

    mounted(){
        this.getTools();
    },

    methods:{
        getTools(){
            getTools().then(res =>{
                this.tools = res.data;
            }).catch(err =>{
                this.$message.error('程序发生错误')
            })
        },
    }
}
</script>

<style lang="scss" scoped>
    .tools{
        margin: 50px 16%;
        li{
            display: inline-block;;
            width: 15%;
            min-width: 150px;
            margin: 4px;
        }
    }
</style>

