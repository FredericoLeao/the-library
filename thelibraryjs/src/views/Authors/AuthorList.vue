<template>
  <div class="row">
    <div class="col-4" style="padding:22px;"
      v-for="(authorItem, i) in authors"
      :key="i">
      <AuthorItem :authorItem="authorItem" @editAuthor="$emit('edit-author', $event)" />
    </div>
  </div>
</template>

<script>
import AuthorItem from '@/views/Authors/AuthorItem'

export default {
  name: 'AuthorList',
  props: ['authors'],
  emits: ['edit-author'],
  components: {
    AuthorItem
  },
  data () {
    return {

    }
  }
}
</script>