<template>
  <div>
    <modal-dialog
      title="Open Library Confirmation"
      ref="olConfirmModal"
      btn-ok-text="Confirm"
      @ok="confirmOLData">
      <div v-if="Object.keys(this.openLibrary).length > 0">
        <div class="row">
          <div class="col-8">
            <h3>
              {{ this.openLibrary.title }}
            </h3>
            <h5>Author(s):</h5>
            <div v-if="openLibraryLoadingAuthors"> Fetching authors data... please wait.</div>
            <div v-else-if="!openLibrary.authorsList">No authors found</div>
            <div v-if="openLibrary.authorsList">
              <div v-for="(author, idx) in openLibrary.authorsList" :key="idx" class="card">
                <div class="card-body">
                  <h5>
                    <span v-if="'personal_name' in author && author.personal_name.length > author.name.length">
                      {{ author.personal_name }}
                    </span>
                    <span v-else>{{ author.name }}</span>
                  </h5>
                  <div v-for="(dbmatch, idj) in author.dbMatches" :key="idj">
                    <input
                      type="radio"
                      :value="dbmatch.id"
                      :id="dbmatch.id"
                      :name="`author_${author.key}_selection`"
                      :checked="author.selectedAuthorOption === dbmatch.id"
                      v-model="author.selectedAuthorOption">
                    <label :for="dbmatch.id" class="px-1">
                      {{ dbmatch.name }} <small>(Use this, already existing in our database)</small>
                    </label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      id="save-new-author-ol-data"
                      value="save-ol-as-new-author"
                      :name="`author_${author.key}_selection`"
                      :checked="author.selectedAuthorOption === 'save-ol-as-new-author'"
                      v-model="author.selectedAuthorOption">
                    <label for="save-new-author-ol-data" class="px-1">
                      Add this Author using this Open Library's Data
                    </label>
                  </div>
                  <div>
                    <input
                      type="radio"
                      id="manually-select-author"
                      value="manually-select-author"
                      :name="`author_${author.key}_selection`"
                      :checked="author.selectedAuthorOption === 'manually-select-author'"
                      v-model="author.selectedAuthorOption">
                    <label for="manually-select-author" class="px-1">
                      I will manually select the author myself
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4">
            <div>
              Cover:
            </div>
            <img :src="openLibrary.cover_url" height="190" />
          </div>
        </div>
      </div>
    </modal-dialog>
    <modal-dialog
      title="Book"
      ref="formModal"
      btn-ok-text="Save"
      @ok="saveInstance">
      <div>
        <div class="row">
          <div class="col-8">
            <div class="row">
              <div class="col-12">
                <label for="book-title">ISBN:</label>
                <small
                  class="float-end"
                  v-if="bookInstance.isbn && bookInstance.isbn.length >= 10">
                  <span v-if="openLibraryLoadingBook">(Fetching data...)</span>
                  <button
                    class="btn btn-link p-0"
                    style="font-size:11px;"
                    @click="lookupByISBN"
                    v-else-if="openLibraryISBNLookup !== bookInstance.isbn.trim()">
                    Fetch from Open Library
                  </button>
                </small>
                <input
                  type="text" id="book-isbn" class="form-control" maxlength="20"
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
                  <template #search="{ attributes, events }">
                    <input
                      class="vs__search"
                      v-bind="attributes"
                      v-on="events"
                      @keyup="handleSearchInput">
                  </template>
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
          </div>
          <div class="col-4">
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
        </div>
      </div>
    </modal-dialog>
    <modal-dialog
      title="Book"
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
      openLibrary: {},
      openLibraryLoadingBook: false,
      openLibraryLoadingAuthors: false,
      openLibraryISBNLookup: '',
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
    handleSearchInput (e) {
      e.target.value = e.target.value.normalize('NFD').replace(/[\u0300-\u036f]/g, "")
      return true
    },

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
            this.authorOptions = response.data.map((author) => { return { value: author.id, label: author.name.normalize('NFD').replace(/[\u0300-\u036f]/g, "") }})
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
      if (this.bookInstance.isbn.trim() < 7) return
      if (this.openLibraryISBNLookup === this.bookInstance.isbn.trim()) return
      this.openLibraryISBNLookup = this.bookInstance.isbn.trim()
      this.openLibraryLoadingBook = true
      this.openLibrary = {}
      axios.get(`http://openlibrary.org/isbn/${this.bookInstance.isbn.trim()}.json`).then((response) => {
        this.openLibraryLoadingBook = false
        if (response.status === 200) {
          this.openLibrary = response.data
          this.openLibrary.cover_url = `http://covers.openlibrary.org/b/id/${response.data.covers[0]}-L.jpg`
          this.loadOpenLibraryAuthors()
          this.$refs.formModal.hide()
          this.$refs.olConfirmModal.show()
        }
      }).catch((axiosObj) => {
        this.openLibraryLoadingBook = false
        const response = axiosObj.response
        if (response.status === 404) {
          console.warn(`OL Book not found: ${this.bookInstance.isbn.trim()}`)
        } else {
          console.warn(`Error (${response.status}) while fetching OL Book (${this.bookInstance.isbn.trim()})`)
        }
      })
    },

    loadOpenLibraryAuthors () {
      if (Object.keys(this.openLibrary).length === 0 ||
          !('authors' in this.openLibrary) ||
          this.openLibrary.authors.length === 0) return ''
      this.openLibrary.authorsList = []
      this.openLibraryLoadingAuthors = true
      // this 'openLibrary.authors' is from the 'book response' and only contains a key to be used to fetch the data
      // and 'openLibrary.authorsList' will be feed bellow, containing the authors prepared data
      this.openLibrary.authors.forEach((author) => {
        axios.get(`http://openlibrary.org${author.key}.json`).then((response) => {
          this.openLibraryLoadingAuthors = false
          if (response.status === 200) {
            const olAuthorData = {
              name: response.data.name,
              key: response.data.key,
              selectedAuthorOption: 'save-ol-as-new-author'
            }
            if ('personal_name' in response.data && response.data.personal_name.length > response.data.name.length) {
              olAuthorData['name'] = response.data.personal_name
            }
            this.openLibrary.authorsList.push(olAuthorData)
            axiosAPI.get('/authors/lookup/', { params: { lookup_string: olAuthorData['name'] }}).then((response) => {
              if (response.status === 200) {
                const dbMatches = response.data.map((authorRes) => {
                  return { id: authorRes.id, name: authorRes.name }
                })
                const _author = this.openLibrary.authorsList.filter((adata) => {
                  if (adata.key === olAuthorData.key) {
                    return true
                  }
                }).shift()
                _author['dbMatches'] = dbMatches
                if (dbMatches.length > 0) {
                  _author['selectedAuthorOption'] = dbMatches[0]['id']
                }
              }
            })
          }
        }).catch((response) => {
          if (response.status === 404) {
            console.warn('OL Author data not found')
          }
        })
      })
    },

    loadBase64ImageFromURL (imageURL) {
      const _this = this
      fetch(imageURL).then((response) => {
        if (response.status === 200) {
          response.blob().then((blob) => {
            var reader = new FileReader()
            reader.addEventListener('load', function() {
              _this.bookInstance.cover = reader.result.toString().replace('data:', '').replace(/^.+,/, '')
            })
            reader.readAsDataURL(blob)
          })
        }
      })
    },

    async confirmOLData () {
      this.bookInstance.title = this.openLibrary.title
      this.bookInstance.description = this.openLibrary.full_title
      this.bookInstance.cover_url = this.openLibrary.cover_url
      this.loadBase64ImageFromURL(this.bookInstance.cover_url)

      if ('authorsList' in this.openLibrary) {
        await Promise.all(this.openLibrary.authorsList.map(async (author) => {
          // clean any previously selected author, as we are asking the user what to do now
          this.bookInstance.authors = []
          if (author.selectedAuthorOption === 'save-ol-as-new-author') {
            let newAuthorData = {
              'name': author.name,
              'description': `${author.name} (** From Open Library)`
            }
            const newAuthorRes = await axios.post('http://localhost/api/authors/', newAuthorData)
            if (newAuthorRes.status === 201) {
              this.bookInstance.authors.push({ id: newAuthorRes.data.id, name: newAuthorRes.data.name })
            }
          } else if (parseInt(author.selectedAuthorOption) > 0 && author.dbMatches.length > 0) {
            this.bookInstance.authors.push(author.dbMatches.filter((dbAuthor) => dbAuthor.id === author.selectedAuthorOption).shift())
          }
          return author
        }))
        this.selectedAuthors = await this.bookInstance.authors.map((author) => {
          return { value: author.id, label: author.name }
        })
      }
      this.$refs.olConfirmModal.hide()
      this.$refs.formModal.show()
    }
  }
}
</script>
