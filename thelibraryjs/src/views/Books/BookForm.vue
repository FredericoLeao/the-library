<template>
  <div>
    <modal-dialog
      title="Add Book"
      ref="formModal"
      btn-ok-text="Salvar"
      @ok="saveInstance">
      <div>
        <div class="row">
          <div class="col-12">
            <label for="book-title">ISBN:</label>
            <input
              type="text" id="book-isbn" class="form-control" maxlength="20"
              @blur="lookupByISBN"
              v-model="bookInstance.isbn">
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
            <v-select
              class="form-control shadow"
              multiple
              id="author-select"
              @search="searchAuthor"
              :options="authorOptions"
              v-model="selectedAuthors">
              <template #option="{ label }">
                {{ label }}
              </template>
              <template #selected-option="{ label }">
                {{ label }}
              </template>
              <template #no-options="">
                <small>
                  Type your search to find some author...
                </small>
              </template>
            </v-select>
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
              v-model="selectedCategories"
              class="form-control shadow">
              <template #option="{ label }">
                {{ label }}
              </template>
              <template #selected-option="{ label }">
                {{ label }}
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
            <label for="book-cover">Cover:</label>
            <input type="file" id="book-cover" class="form-control" @change="loadFile($event, 'cover')">
          </div>
        </div>
        <div class="row mt-1" v-if="bookInstance.cover_url">
          <div class="col-12">
            <img :src="bookInstance.cover_url" style="height:190px;">
          </div>
        </div>
      </div>
    </modal-dialog>
    <modal-dialog
      title="Book Form"
      ref="formResponseModal"
      btn-ok-text="Fechar"
      :btn-cancel-visible="false"
      @ok="$refs.formResponseModal.hide()">
      <div v-if="responseStatus===201">Book was created</div>
      <div v-else-if="responseStatus===200">Book's data was saved</div>
      <div v-else-if="responseStatus">Error... this system may need a doctor</div>
    </modal-dialog>
  </div>
</template>

<script>
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'
import { axiosAPI } from '@/axios'
import ModalDialog from '@/components/Modal.vue'
import FormMixin from '@/mixins/FormMixin'
import axios from 'axios'

export default {
  name: 'BookForm',
  mixins: [FormMixin],
  emits: ['update-books'],
  props: ['bookLoad'],

  components: {
    vSelect,
    ModalDialog
  },

  mounted () {
    this.formReset()
  },

  watch: {
    bookLoad (newValue) {
      if (newValue) {
        this.bookInstance = Object.assign({}, newValue)
        // must arrange authors and categories
        this.selectedCategories = this.bookInstance.categories.map((cat) => {
          return { value: cat.id, label: cat.name }
        })
        this.selectedAuthors = this.bookInstance.authors.map((author) => {
          return { value: author.id, label: author.name }
        })
      }
    }
  },

  data () {
    return {
      instanceName: 'books',
      bookInstance: {},
      bookModelObject: {
        title: '',
        isbn: '',
        description: '',
        authors: [],
        categories: [],
        authors_ids: [],
        categories_ids: [],
        cover: ''
      },
      selectedAuthors: [],
      selectedCategories: [],
      authorOptions: [],
      categoryOptions: [],
    }
  },

  computed: {
    loadedInstance () {
      return this.bookInstance
    }
  },

  methods: {
    prepareFormData () {
      this.bookInstance.authors_ids = this.selectedAuthors.map(author => author.value)
      this.bookInstance.categories_ids = this.selectedCategories.map(category => category.value)
    },

    searchCategory (search) {
      this.categoryOptions = []
      if (search.length > 2) {
        axiosAPI.get(`/categories/lookup/`, { params: { lookup_string: search }})
        .then(response => {
          if (response.status === 200) {
            this.categoryOptions = response.data.map(category => { return { value: category.id, label: category.name }})
          }
        })
      }
    },

    searchAuthor (search) {
      this.authorOptions = []
      if (search.length > 2) {
        axiosAPI.get('/authors/lookup/', { params: { lookup_string: search }})
        .then(response => {
          if (response.status === 200) {
            this.authorOptions = response.data.map(author => { return { value: author.id, label: author.name }})
          }
        })
      }
    },

    formReset () {
      this.selectedAuthors = []
      this.selectedCategories = []
      this.bookInstance = Object.assign({}, this.bookModelObject)
    },

    lookupByISBN () {
      axios.get(`http://openlibrary.org/isbn/${this.bookInstance.isbn}.json`).then((response) => {
        if (response.status === 200) {
          console.log(response.data)
          this.bookInstance.title = response.data.title
          this.bookInstance.description = response.data.full_title
          if (response.data.covers.length > 0) {
            this.bookInstance.cover_url = `http://covers.openlibrary.org/b/id/${response.data.covers[0]}-L.jpg`
            this.loadBase64ImageFromURL(this.bookInstance.cover_url)
          }
        }
      })
    },
    loadBase64ImageFromURL (imageURL) {
      const _this = this
      fetch(imageURL).then((response) => {
        if (response.status === 200) {
          response.blob().then((blob) => {
            console.log(blob)
            var reader = new FileReader()
            reader.addEventListener('load', function() {
              _this.bookInstance.cover = reader.result.toString().replace('data:', '').replace(/^.+,/, '')
            })
            reader.readAsDataURL(blob)
          })
        }
      })
    }
  }
}
</script>
