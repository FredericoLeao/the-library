<template>
  <div class="container">
    <modal-dialog
      title="Add Book"
      ref="bookFormModal">
      <book-form />
    </modal-dialog>
    <div>
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="col-12">
        <div class="float-end">
          <button class="btn btn-primary" @click="$refs.bookFormModal.show()">Add Book</button>
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
import ModalDialog from '@/components/Modal.vue'
import axios from 'axios'

export default {
  name: 'BookIndex',
  components: {
    BookList,
    HeaderMenu,
    BookForm,
    ModalDialog
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