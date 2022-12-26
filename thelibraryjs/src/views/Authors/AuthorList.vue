<template>
  <div class="row">
    <div class="col-4"
      v-for="(authorItem, i) in authors"
      :key="i">
      <AuthorItem :authorItem="authorItem" />
    </div>
  </div>
</template>

<script>
import AuthorItem from '@/views/Authors/AuthorItem'

export default {
  name: 'AuthorList',
  props: ['authors'],
  components: {
    AuthorItem
  },
  data () {
    return {

    }
  }
}
</script>