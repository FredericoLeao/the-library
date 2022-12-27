<template>
  <div class="row">
    <div class="col-4"
      v-for="(categoryItem, i) in categories"
      :key="i">
      <CategoryItem :categoryItem="categoryItem" />
    </div>
  </div>
</template>

<script>
import CategoryItem from '@/views/Categories/CategoryItem'

export default {
  name: 'CategoryList',
  props: ['categories'],
  components: {
    CategoryItem
  },
  data () {
    return {

    }
  }
}
</script>
