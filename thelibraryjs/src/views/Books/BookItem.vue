<template>
  <div class="card">
    <div class="card-body text-center">
      <h3>{{ bookItem.title }}</h3>
      <div v-if="bookItem.authors.length > 0">{{ bookItem.authors[0].name }}</div>
      <div v-else>(Missing author's name)</div>
      <div v-if="bookItem.categories.length > 0">{{ bookItem.categories[0].name }}</div>
      <div v-else>(Missing category)</div>
      <div v-if="!bookItem.cover" style="padding:32px;background-color:#eee;">
        <i class="bi bi-book" style="font-size:154px;"></i>
      </div>
      <div v-else class="p-3">
        <img :src="bookItem.cover" style="width:260px;height:260px;">
      </div>
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