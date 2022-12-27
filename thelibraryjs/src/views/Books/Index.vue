<template>
  <div class="container">
    <book-form ref="bookForm" />
    <div>
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="col-12">
        <div class="float-end">
          <button class="btn btn-primary" @click="$refs.bookForm.show()">Add Book</button>
        </div>
      </div>
    </div>
    <BookList :books="books"></BookList>
  </div>
</template>

<script>
import BookList from '@/views/Books/BookList'
import BookForm from '@/views/Books/BookForm'
import HeaderMenu from '@/components/HeaderMenu'
import axios from 'axios'

export default {
  name: 'BookIndex',
  components: {
    BookList,
    HeaderMenu,
    BookForm
  },
  data () {
    return {
      books: [],
    }
  },

  mounted () {
    this.getBooks()
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