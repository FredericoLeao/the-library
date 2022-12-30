<template>
  <div>
    <modal-dialog
      title="Category Form"
      ref="formModal"
      btn-ok-text="Salvar"
      @ok="saveInstance">
      <div class="row">
        <div class="col-12">
          <label for="category-name">Nome:</label>
          <input type="text" id="category-name" class="form-control" maxlength="150" v-model="categoryInstance.name">
        </div>
      </div>
    </modal-dialog>
    <modal-dialog
      title="Category Form"
      ref="formResponseModal"
      btn-ok-text="Fechar"
      :btn-cancel-visible="false"
      @ok="$refs.formResponseModal.hide()">
      <div v-if="responseStatus===201">Category's data was saved</div>
      <div v-else-if="responseStatus && responseStatus!==201">Error... this system may need a doctor</div>
    </modal-dialog>
  </div>
</template>

<script>
import ModalDialog from '@/components/Modal.vue'
import FormMixin from '@/mixins/FormMixin'

export default {
  name: 'CategoryForm',
  props: ['category'],
  emits: ['update-categories'],
  mixins: [FormMixin],

  components: {
    ModalDialog
  },

  data () {
    return {
      instanceName: 'categories',
      categoryInstance: {
        id: null,
        name: ''
      },
    }
  },

  computed: {
    loadedInstance () {
      return this.categoryInstance
    }
  }
}
</script>
