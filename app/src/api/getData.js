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

/*删除文章*/
export const delArticle = (id) =>{
    return request('/blog/api/article/delete?id='+ id);
}

/*获取图片*/
export const getImage = (id) =>{
    return request('/blog/api/image/query', json);
}