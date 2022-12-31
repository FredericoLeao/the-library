<template>
  <div class="card">
    <div class="card-body">
      <i
        class="bi bi-pencil-square float-end"
        style="cursor: pointer;"
        @click="$emit('edit-category', this.categoryItem)">
      </i>
      <h3>
        {{ categoryItem.name }}
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