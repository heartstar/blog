import request from '@/utils/request'

/*获取文章类型*/
export const getMenu = () =>{
    return request('/blog/api/menu')
}

/*新增文章*/
export const addArticle = (json) =>{
    return request('/blog/api/article/add', json, 'POST');
}

/*获取文章列表*/
export const getArticle = (json) =>{
    return request('/blog/api/article/query', json);
}

/*搜索文章*/
export const searArticle = (json) =>{
    return request('/blog/api/article/search', json);
}

/*获取文章详情*/
export const getArticleDetail = (json) =>{
    return request('/blog/api/article/detail', json);
}

/*删除文章*/
export const delArticle = (id) =>{
    return request('/blog/api/article/delete?id='+ id);
}

/*获取图片*/
export const getImage = (json) =>{
    return request('/blog/api/image/query', json);
}

/*发送消息*/
export const sendMsg = (json) =>{
    return request('/blog/api/msg/send', json);
}

/*获取工具集*/
export const getTools = (json) =>{
    return request('/blog/api/tools/query', json);
}

/*获取电影集*/
export const getMovies = (json) =>{
    return request('/blog/api/movie/query', json);
}