<template>
  <div class="row">
    <div class="col-4" style="padding:22px;"
      v-for="(categoryItem, i) in categories"
      :key="i">
      <CategoryItem :categoryItem="categoryItem" @editCategory="$emit('edit-category', $event)"/>
    </div>
  </div>
</template>

<script>
import CategoryItem from '@/views/Categories/CategoryItem'

export default {
  name: 'CategoryList',
  props: ['categories'],
  emits: ['edit-category'],

  components: {
    CategoryItem
  },
  data () {
    return {

    }
  }
}
</script>
