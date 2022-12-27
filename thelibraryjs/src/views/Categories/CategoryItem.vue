<template>
  <div class="card">
    <div class="card-body">
      <h2>
        {{  categoryItem.name }}
      </h2>
      ({{  categoryItem.id }})
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