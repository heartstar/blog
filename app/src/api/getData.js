import request from '@/utils/request'

/*获取首页菜单信息*/
export const getMenu = () =>{
    return request('/blog/api/menu')
}

/*新增文章*/
export const addArticle = (json) =>{
    return request('/blog/api/article', json, 'POST');
}

/*获取文章列表*/
export const getArticle = (json) =>{
    return request('/blog/api/article');
}