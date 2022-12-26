<template>
  <div>
    <div class="row">
      <div class="col-12">
        <label for="book-title">ISBN:</label>
        <input type="text" id="book-isbn" class="form-control" maxlength="20">
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <label for="book-title">Title:</label>
        <input type="text" id="book-title" class="form-control">
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <label for="book-title">Description:</label>
        <textarea id="book-description" class="form-control"></textarea>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <label for="book-authors">Authors:</label>
        <input type="text" id="book-authors" class="form-control">
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <label for="book-authors">Categories:</label>
        <input type="text" id="book-authors" class="form-control">
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <label for="book-cover">Capa:</label>
        <input type="file" id="book-cover" class="form-control">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookForm',

  data () {
    return {
      
    }
  }
}
</script>