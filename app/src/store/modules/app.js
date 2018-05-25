
const app = {
    state: {    
        loading: false,
        isLogin: false,
    },
    mutations: {
        SET_LOADING: (state, status) =>{
            state.loading = status;
        },

        SET_LOGIN: (state, status) =>{
            state.isLogin = status;
        }

    },
    actions: {
        setLoading({ commit }, status){
            commit('SET_LOADING', status);
        },  
        
        setLogin({ commit }, status){
            commit('SET_LOGIN', status);
        }, 
    }
}

export default app
