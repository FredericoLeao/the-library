<template>
  <BookList :books="books"></BookList>
</template>

<script>
import BookList from '@/views/Books/BookList'
import axios from 'axios'
export default {
  name: 'BookIndex',
  components: {
    BookList
  },
  data () {
    return {
      books: [],
    }
  },

  mounted () {
    this.getBooks()
    console.log("HELOOOO")
  },

  methods: {
    getBooks () {
      axios.get('http://localhost/api/books/').then((response) => {
        if (response.status === 200) {
          this.books = response.data
        }
      })
    }
  }
}
</script>