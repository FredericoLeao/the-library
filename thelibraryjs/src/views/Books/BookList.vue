<template>
  <div>
    <BookItem
      v-for="(bookItem, i) in books"
      :key="i"
      :bookItem="bookItem" />
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