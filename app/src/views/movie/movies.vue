<template>
    <div>
        <section class="movies">
            <ul class="nav">
                <li v-for="(item, index) in movies" :key="index">
                    <a :href="item.href" class="link" target="_blank">
                        <div class="img">
                            <img :src="item.img" :alt="item.title">
                        </div>
                        <div class="info">
                            <p>{{ item.title }}</p>
                        </div>
                    </a>
                </li>
            </ul>
        </section>
    </div>
</template>

<script>
import { getMovies } from '@/api/getData'
export default {
    name: 'movies',
    components:{

    },
    data() {
        return {
            movies: null,
        };
    },

    mounted(){
        this.getMovies();
    },

    methods:{
        getMovies(){
            getMovies().then(res =>{
                this.movies = res.data;
            }).catch(err =>{
                this.$message.error('程序发生错误')
            })
        },
    }
}
</script>

<style lang="scss" scoped>
.movies{
    width: 1000px;
    margin: auto;
    li{
        display: inline-block;;
        margin: 20px 20px 0px 0;
        a.link{
            text-align: center;
            .img{
                width: 170px;
                height: 224px;
                img{
                    width: 100%;
                    height: 100%;
                }
            }
        }
    }
}
</style>

