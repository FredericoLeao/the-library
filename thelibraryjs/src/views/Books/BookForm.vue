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
            <label for="book-cover">Capa:</label>
            <input type="file" id="book-cover" class="form-control" @change="loadFile($event, 'cover')">
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
      <div v-if="responseStatus===201">Book's data was saved</div>
      <div v-else-if="responseStatus && responseStatus!==201">Error... this system may need a doctor</div>
    </modal-dialog>
  </div>
</template>

<script>
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'
import { axiosAPI } from '@/axios'
import ModalDialog from '@/components/Modal.vue'
import FormMixin from '@/mixins/FormMixin'

export default {
  name: 'BookForm',
  mixins: [FormMixin],
  emits: ['update-books'],

  components: {
    vSelect,
    ModalDialog
  },

  data () {
    return {
      instanceName: 'books',
      bookInstance: {
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
  }
}
</script>
