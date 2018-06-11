<template>
	<div class="article">
		<div class="search">
			<i class="el-icon-search" @click="search"></i>
		</div>
		<div v-if="(pageTotal)">
			<div class="cards">
				<el-card class="box-card" shadow="hover" v-for="(item, index) in dataList" :key="index" >
					<div class="text item" @click="goDetail(item.articleId)">
						<h4>{{ item.title }}</h4>
						<h6>{{ item.keyword }}</h6>
						<p>{{ item.content.substring(0, 300)+"..." }}</p>
						<div class="card-footer">
							<span class="visits">阅读({{ item.visits }})</span>
							<el-date-picker v-if="Boolean(item.update_time)" v-model="item.update_time" size="mini" type="datetime" disabled placeholder=""></el-date-picker>
						</div>
					</div>
				</el-card>
			</div>
			<el-pagination
				v-if="(pageTotal>page.pageSize)"
				@current-change="handleCurrentChange"
				:page-size="page.pageSize"
				layout="total, prev, pager, next, jumper"
				:total="pageTotal">
			</el-pagination>
		</div>
		<center class="noHave" v-else>暂无数据</center>
		<el-dialog title="搜索" :visible.sync="searchShow" width="30%">
			<el-input v-model="searchStr" ref="seCon" placeholder="请输入需要搜索的文章内容" @keyup.enter.native="onSearch(searchStr)"></el-input>
		</el-dialog>
	</div>
</template>

<script>
import { getMenu, getArticle, searArticle } from '@/api/getData'

export default {
	name: 'articleList',

	data() {
		return {
			dataList: null,
			searchStr: '',
			searchShow: false,
			pageTotal: null,
			page: {
				paramsId: '',
				pageNum: 1,
				pageSize: 12,
			},
		}
	},

	created() {

		if(Boolean(this.$route.params)){
			this.page.paramsId = this.$route.params.id
		}

		getMenu().then(res =>{
			this.types = res.data;
		}).catch(err =>{})

		this.init();

	},

	methods: {

		init(){

			getArticle(this.page).then(res =>{
				this.dataList = res.data;
				this.pageTotal = res.total;
			}).catch(err =>{})

		},

		goDetail(id){
			this.$router.push({path: '/article/detail', query:{'id': id}});
		},

		handleSelectionChange(row){
			this.selected = row;
		},

		handleCurrentChange(index){
			this.page.pageNum = index;
			this.init();
		},

		search(){
			this.searchShow = true;
			this.$nextTick(() =>{
				this.$refs.seCon.focus();
			});
		},

		onSearch(str){
			searArticle({'str':str}).then(res =>{
				this.dataList = res.data;
				this.pageTotal = res.total;
				this.searchShow = false;
			}).catch(err =>{})
		},
	},

	watch:{
		$route(val){
			if(val.params){
				this.page.paramsId = val.params.id;
				this.init();
			}
		}
	}
}
</script>

<style lang="scss">
	.el-card{
		width: 32%;
		float: left;
		margin: 0.5%;
		cursor: pointer;
		position: relative;
		height: 300px;
		.card-footer{
			position: absolute;
			right: 0px;
			bottom: 0px;
			.el-date-editor{
				width: 120px;
			}
			.visits{
				font-size: 12px;
				color: #c0c4cc;
				margin: 0 25px 0 0;
			}
		}
		h4:hover{
			text-decoration: underline;
			color: #38f;
		}
	}
	.noHave{
		color: #c0c4cc;
		margin: 80px;
	}
	.el-pagination{
		clear: both;
		margin: 20px 0;
		text-align: center;
	}
	.search{
		position: absolute;
		right: 40px;
		top: 22px;
		z-index: 10;
		.el-icon-search{
			transform: scale(1.2);
			cursor: pointer;
			color: #0084ff;
		}
	}
</style>

