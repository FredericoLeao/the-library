<template>
  <div class="container">
    <div>
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="col-12">
        <div class="float-end">
          <button class="btn btn-primary">Add Book</button>
        </div>
      </div>
    </div>
    <BookList :books="books"></BookList>
  </div>
</template>

<script>
import BookList from '@/views/Books/BookList'
import HeaderMenu from '@/views/HeaderMenu'
import axios from 'axios'

export default {
  name: 'BookIndex',
  components: {
    BookList,
    HeaderMenu
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