<template>
  <div>
    <modal-dialog
      title="Category Form"
      ref="categoryFormModal"
      btn-ok-text="Salvar"
      @ok="okButton()">
      <div class="row">
        <div class="col-12">
          <label for="category-name">Nome:</label>
          <input type="text" id="category-name" class="form-control" maxlength="150" v-model="categoryInstance.name">
        </div>
      </div>
    </modal-dialog>
    <modal-dialog
      title="Category Form"
      ref="categoryFormResponseModal"
      btn-ok-text="Fechar"
      :btn-cancel-visible="false"
      @ok="$refs.categoryFormResponseModal.hide()">
      <div v-if="responseStatus===201">Category's data was saved</div>
      <div v-else-if="responseStatus && responseStatus!==201">Error... this system may need a doctor</div>
    </modal-dialog>
  </div>
</template>

<script>
import ModalDialog from '@/components/Modal.vue'
import axios from 'axios'

export default {
  name: 'CategoryForm',
  props: ['category'],
  emits: ['update-categories'],
  components: {
    ModalDialog
  },
  data () {
    return {
      categoryInstance: {
        id: null,
        name: ''
      },
      responseStatus: null
    }
  },

  methods: {
    saveInstance () {
      if (!this.categoryInstance.id) {
        axios.post('http://localhost/api/categories/', this.categoryInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 201) {
            this.$emit('update-categories')
            this.hide()
            this.showFormResponse()
          }
        })
      } else {
        axios.put(`http://localhost/api/categories/${this.categoryInstance.id}/`, this.categoryInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 200) {
            // emit update object
          }
        })
      }
    },

    hide () {
      this.$refs.categoryFormModal.hide()
    },
    show () {
      this.$refs.categoryFormModal.show()
    },
    showFormResponse () {
      this.$refs.categoryFormResponseModal.show()
    },
    hideFormResponse () {
      this.$refs.categoryFormResponseModal.hide()
    },

    okButton () {
      this.saveInstance()
    }
  }
}
</script>
