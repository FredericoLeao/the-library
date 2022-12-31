<template>
  <div class="container">
    <category-form ref="categoryForm" @updateCategories="getCategories()" :categoryLoad="categoryLoad" />
    <div>
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="col-12">
        <div class="float-end">
          <button class="btn btn-primary" @click="addCategory">Add Category</button>
        </div>
      </div>
    </div>
    <CategoryList :categories="categories" @editCategory="editCategory"></CategoryList>
  </div>
</template>

<script>
import CategoryList from '@/views/Categories/CategoryList'
import CategoryForm from '@/views/Categories/CategoryForm'
import HeaderMenu from '@/components/HeaderMenu'
import { axiosAPI } from '@/axios'

export default {
  name: 'CategoryIndex',
  components: {
    CategoryList,
    HeaderMenu,
    CategoryForm
  },
  data () {
    return {
      categories: [],
      categoryLoad: {}
    }
  },

  mounted () {
    this.getCategories()
  },

  methods: {
    getCategories () {
      axiosAPI.get('/categories/').then((response) => {
        if (response.status === 200) {
          this.categories = response.data
        }
      })
    },

    editCategory (category) {
      this.categoryLoad = Object.assign({}, category)
      this.$refs.categoryForm.show()
    },

    addCategory () {
      this.$refs.categoryForm.formReset()
      this.$refs.categoryForm.show()
    }
  }
}
</script>
