<template>
  <div class="card">
    <div class="card-body">
      <h3>{{ categoryItem.name }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CategoryItem',
  props: ['categoryItem'],

  data () {
    return {
      
    }
  }
}
</script>