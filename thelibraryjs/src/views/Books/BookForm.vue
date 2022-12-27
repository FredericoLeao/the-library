<template>
  <modal-dialog
    title="Add Book"
    ref="bookFormModal">
    <div>
      <div class="row">
        <div class="col-12">
          <label for="book-title">ISBN:</label>
          <input type="text" id="book-isbn" class="form-control" maxlength="20">
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-title">Title:</label>
          <input type="text" id="book-title" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-title">Description:</label>
          <textarea id="book-description" class="form-control"></textarea>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-authors">Authors:</label>
          <vSelect
            multiple
            id="author-select"
            @search="searchAuthor"
            :options="authorOptions"
            v-model="bookInstance.authors"
            label="name"
            class="form-control shadow">
            <template #option="{ name }">
              {{ name }}
            </template>
            <template #selected-option="{ name }">
              {{ name }}
            </template>
            <template #no-options="">
              <small>
                Type your search to find some author...
              </small>
            </template>
          </vSelect>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-authors">Categories:</label>
          <input type="text" id="book-authors" class="form-control">
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-cover">Capa:</label>
          <input type="file" id="book-cover" class="form-control">
        </div>
      </div>
    </div>
  </modal-dialog>
</template>

<script>
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'
import axios from 'axios'
import ModalDialog from '@/components/Modal.vue'

export default {
  name: 'BookForm',
  components: {
    vSelect,
    ModalDialog
  },

  data () {
    return {
      bookInstance: {
        authors: [],
      },
      authorOptions: []
    }
  },

  methods: {
    searchAuthor (search) {
      this.authorOptions = []
      if (search.length > 2) {
        axios.get('http://localhost/api/authors/lookup/', { params: { lookup_string: search }})
        .then(response => {
          if (response.status === 200) {
            this.authorOptions = response.data
          }
        })
      }
    },

    hide () {
      this.$refs.bookFormModal.hide()
    },

    show () {
      this.$refs.bookFormModal.show()
    },

    //showFormResponse () {
    //  this.$refs.authorFormResponseModal.show()
    //},
//
    //hideFormResponse () {
    //  this.$refs.authorFormResponseModal.hide()
    //}

  }
}
</script>