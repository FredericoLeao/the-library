<template>
  <div class="card">
    <div class="card-body">
      <h3>
        {{ categoryItem.name }}
        <i class="bi bi-pencil-square float-end" @click="$emit('edit-category', this.categoryItem)"></i>
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CategoryItem',
  props: ['categoryItem'],
  emits: ['edit-category'],

  data () {
    return {
      
    }
  }
}
</script>