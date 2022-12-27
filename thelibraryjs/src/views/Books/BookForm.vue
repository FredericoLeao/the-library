<template>
  <modal-dialog
    title="Add Book"
    ref="bookFormModal"
    btn-ok-text="Salvar"
    @ok="okButton()">
    <div>
      <div class="row">
        <div class="col-12">
          <label for="book-title">ISBN:</label>
          <input type="text" id="book-isbn" class="form-control" maxlength="20" v-model="bookInstance.isbn">
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-title">Title:</label>
          <input type="text" id="book-title" class="form-control" v-model="bookInstance.title">
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="book-title">Description:</label>
          <textarea id="book-description" class="form-control" v-model="bookInstance.description"></textarea>
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
          <label for="book-categories">Categories:</label>
          <vSelect
            multiple
            id="category-select"
            @search="searchCategory"
            :options="categoryOptions"
            v-model="bookInstance.categories"
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
                Type your search to find some category...
              </small>
            </template>
          </vSelect>
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
        title: '',
        isbn: '',
        description: '',
        authors: [],
        categories: [],
        cover: ''
      },
      authorOptions: [],
      categoryOptions: []
    }
  },

  methods: {
    searchCategory (search) {
      this.categoryOptions = []
      if (search.length > 2) {
        axios.get('http://localhost/api/categories/lookup/', { params: { lookup_string: search }})
        .then(response => {
          if (response.status === 200) {
            this.categoryOptions = response.data
          }
        })
      }
    },

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

    saveInstance () {
      if (!this.bookInstance.id) {
        axios.post('http://localhost/api/books/', this.bookInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 201) {
            this.$emit('update-books')
            this.hide()
            this.showFormResponse()
          }
        })
      } else {
        axios.put(`http://localhost/api/books/${this.bookInstance.id}/`, this.bookInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 200) {
            // emit update object
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
    okButton () {
      this.saveInstance()
    }
  }
}
</script>