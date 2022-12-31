<template>
  <div class="card">
    <div class="card-body">
      <i class="bi bi-pencil-square float-end" style="cursor:pointer;" @click="editAuthor"></i>
      <h2>
        {{  authorItem.name }}
      </h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthorItem',
  props: ['authorItem'],
  emits: ['edit-author'],

  data () {
    return {
      
    }
  },

  methods: {
    editAuthor () {
      this.$emit('edit-author', this.authorItem)
    }
  }
}
</script>