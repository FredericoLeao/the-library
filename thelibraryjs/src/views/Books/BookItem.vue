<template>
  <div>
    <h2>
      {{  bookItem.name }}
    </h2>
    <br>{{  bookItem.id }}
    <br>------------------------
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