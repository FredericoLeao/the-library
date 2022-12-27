<template>
  <div class="card">
    <div class="card-body text-center">
      <h3>{{ bookItem.title }}</h3>
      <div v-if="bookItem.authors.length > 0">{{ bookItem.authors[0].name }}</div>
      <div v-if="bookItem.categories.length > 0">({{ bookItem.categories[0].name }})</div>
      <i v-if="!bookItem.cover" class="bi bi-book" style="font-size:190px;"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookItem',
  props: ['bookItem'],

  data () {
    return {
      
    }
  }
}
</script>