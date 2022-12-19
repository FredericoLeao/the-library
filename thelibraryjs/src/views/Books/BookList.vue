<template>
  <div class="row">
    <div class="col-4"
      v-for="(bookItem, i) in books"
      :key="i">
      <BookItem :bookItem="bookItem" />
    </div>
  </div>
</template>

<script>
import BookItem from '@/views/Books/BookItem'

export default {
  name: 'BookList',
  props: ['books'],
  components: {
    BookItem
  },
  data () {
    return {

    }
  }
}
</script>