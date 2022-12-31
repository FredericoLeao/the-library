<template>
  <div class="container">
    <book-form ref="bookForm" @updateBooks="getBooks()" :bookLoad="bookLoad" />
    <div>
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="col-12">
        <div class="float-end">
          <button class="btn btn-primary" @click="addBook">Add Book</button>
        </div>
      </div>
    </div>
    <BookList :books="books" @editBook="editBook"></BookList>
  </div>
</template>

<script>
import BookList from '@/views/Books/BookList'
import BookForm from '@/views/Books/BookForm'
import HeaderMenu from '@/components/HeaderMenu'
import { axiosAPI } from '@/axios'

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
      bookLoad: {}
    }
  },

  mounted () {
    this.getBooks()
  },

  methods: {
    getBooks () {
      axiosAPI.get('/books/').then((response) => {
        if (response.status === 200) {
          this.books = response.data
        }
      })
    },

    editBook (e) {
      this.bookLoad = Object.assign({}, e)
      this.bookLoad.cover_url = this.bookLoad.cover
      this.bookLoad.cover = ''
      this.$refs.bookForm.show()
    },

    addBook () {
      this.$refs.bookForm.formReset()
      this.$refs.bookForm.show()
    }
  }
}
</script>

<style>
.vs__dropdown-toggle {
  border: none !important;
}
</style>
