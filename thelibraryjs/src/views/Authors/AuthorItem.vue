<template>
  <div class="card">
    <div class="card-body">
      <h2>
        {{  authorItem.name }}
        <i class="bi bi-pencil-square float-end" style="cursor:pointer;" @click="editAuthor"></i>
      </h2>
      ({{  authorItem.id }})
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