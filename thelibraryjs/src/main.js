import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { vMaska } from 'maska'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'


const app = createApp(App)
app.directive('maska', vMaska)
app.use(router)
app.mount('#app')
