<template>
  <div class="container">
    <author-form ref="authorForm" @updateAuthors="getAuthors()" />
    <div>
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="col-12">
        <div class="float-end">
          <button class="btn btn-primary" @click="$refs.authorForm.show()">Add Author</button>
        </div>
      </div>
    </div>
    <AuthorList :authors="authors"></AuthorList>
  </div>
</template>

<script>
import AuthorList from '@/views/Authors/AuthorList'
import AuthorForm from '@/views/Authors/AuthorForm'
import HeaderMenu from '@/components/HeaderMenu'
import { axiosAPI } from '@/axios'

export default {
  name: 'AuthorIndex',
  components: {
    AuthorList,
    HeaderMenu,
    AuthorForm
  },
  data () {
    return {
      authors: [],
    }
  },

  mounted () {
    this.getAuthors()
  },

  methods: {
    getAuthors () {
      axiosAPI.get(`/authors/`).then((response) => {
        if (response.status === 200) {
          this.authors = response.data
        }
      })
    },
  }
}
</script>
