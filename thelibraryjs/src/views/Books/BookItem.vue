<template>
  <div class="card">
    <div class="card-body">
      <h2>
        {{  bookItem.title }}
      </h2>
      ({{  bookItem.id }})
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookItem',
  props: ['bookItem'],

  data () {
    return {
      
    }
  }
}
</script>