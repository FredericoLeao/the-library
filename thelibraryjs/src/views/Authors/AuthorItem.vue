<template>
  <div class="card">
    <div class="card-body">
      <h2>
        {{  authorItem.name }}
      </h2>
      ({{  authorItem.id }})
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthorItem',
  props: ['authorItem'],

  data () {
    return {
      
    }
  }
}
</script>