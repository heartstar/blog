
const app = {
    state: {    
        loading: false,
    },
    mutations: {
        SET_LOADING: (state, status) =>{
            state.loading = status;
        },

    },
    actions: {
        setLoading({ commit }, status){
            commit('SET_LOADING', status);
        },       
    }
}

export default app
