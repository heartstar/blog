import request from '@/utils/request'

/*获取首页菜单信息*/
export const getMenu = () =>{
    return request('/sso/seniorsSoft')
}